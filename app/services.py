import requests
from app.config import GITHUB_TOKEN, GRAPHQL_URL

def assign_rating(total_contributions):
    if total_contributions >= 1000:
        return 'A'
    elif total_contributions >= 750:
        return 'B'
    elif total_contributions >= 300:
        return 'C'
    elif total_contributions >= 250:
        return 'D'
    elif total_contributions >= 100:
        return 'E'
    else:
        return 'F'

def fetch_github_data(username):
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }

    # Fetch user profile (followers, following, etc.)
    user_response = requests.get(f'https://api.github.com/users/{username}', headers=headers)
    if user_response.status_code != 200:
        return {'error': 'Unable to fetch user data'}

    user_data = user_response.json()

    # Fetch repos data
    repos_response = requests.get(f'https://api.github.com/users/{username}/repos', headers=headers)
    if repos_response.status_code != 200:
        return {'error': 'Unable to fetch repository data'}

    repos_data = repos_response.json()
    total_followers = user_data.get('followers', 0)
    total_following = user_data.get('following', 0)
    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos_data)

    # Call without headers now
    total_commits = get_total_commits(username)
    total_prs = get_total_pull_requests(username, headers)
    merged_prs = get_merged_pull_requests(username, headers)
    pr_reviewed = get_total_pr_reviewed(username, headers)
    issues = get_total_issues(username, headers)
    discussions_started = get_total_discussions_started(username, headers)
    discussions_answered = get_total_discussions_answered(username, headers)

    # Fetch total contributions over all years using GraphQL
    total_contributions = get_total_contributions(username)

    merged_pr_percentage = (merged_prs / total_prs * 100) if total_prs > 0 else 0

    # Calculate rating based on total contributions
    rating = assign_rating(total_contributions)

    return {
        'username': username,
        'total_stars': total_stars,
        'total_commits': total_commits,
        'total_prs': total_prs,
        'merged_prs': merged_prs,
        'merged_pr_percentage': merged_pr_percentage,
        'pr_reviewed': pr_reviewed,
        'issues': issues,
        'discussions_started': discussions_started,
        'discussions_answered': discussions_answered,
        'total_followers': total_followers,
        'total_following': total_following,
        'total_contributions': total_contributions,
        'rating': rating
    }

# Additional helper functions for GitHub API requests

def get_total_commits(username):
    # GraphQL query to fetch contribution years
    query = """
    query ($username: String!) {
        user(login: $username) {
            contributionsCollection {
                contributionYears
            }
        }
    }
    """
    
    variables = {"username": username}
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    
    response = requests.post(GRAPHQL_URL, json={'query': query, 'variables': variables}, headers=headers)
    
    # Log the full response for debugging purposes
    try:
        response_data = response.json()
    except ValueError:
        print(f"Failed to parse response as JSON. Response text: {response.text}")
        return 0

    # Check if 'data' key exists
    if 'data' not in response_data:
        print(f"Error: 'data' key missing in the response. Full response: {response_data}")
        return 0
    
    try:
        contribution_years = response_data['data']['user']['contributionsCollection']['contributionYears']
    except KeyError:
        print("Error: contribution years not found in the response.")
        return 0
    
    total_commits = 0
    
    # Iterate through each year to calculate total commits
    for year in contribution_years:
        year_query = """
        query ($username: String!, $startDate: DateTime!, $endDate: DateTime!) {
            user(login: $username) {
                contributionsCollection(from: $startDate, to: $endDate) {
                    totalCommitContributions
                    contributionCalendar {
                        totalContributions
                    }
                    commitContributionsByRepository {
                        contributions {
                            totalCount
                        }
                    }
                }
            }
        }
        """
        year_variables = {
            "username": username,
            "startDate": f"{year}-01-01T00:00:00Z",
            "endDate": f"{year}-12-31T23:59:59Z"
        }
        
        year_response = requests.post(GRAPHQL_URL, json={'query': year_query, 'variables': year_variables}, headers=headers)
        
        try:
            year_data = year_response.json()
        except ValueError:
            print(f"Failed to parse year response as JSON. Response text: {year_response.text}")
            continue
        
        if 'data' not in year_data:
            print(f"Error: 'data' key missing in the year response. Full response: {year_data}")
            continue
        
        try:
            contributions_collection = year_data['data']['user']['contributionsCollection']
            total_commit_contributions = contributions_collection.get('totalCommitContributions', 0)
            total_contributions = contributions_collection['contributionCalendar']['totalContributions']
            
            if total_commit_contributions == 0:  # Using fallback estimation
                # Estimate commits using total contributions and percentage of commits
                commit_percentage = calculate_commit_percentage(username, headers, year_variables)
                estimated_commits = int(total_contributions * (commit_percentage / 100))
                total_commits += estimated_commits
            else:
                total_commits += total_commit_contributions
        
        except KeyError:
            print(f"Error extracting commit data for year {year}.")
    
    return total_commits

# Fallback function to estimate commit percentage if no exact commit data is available
def calculate_commit_percentage(username, headers, year_variables):
    # This function estimates the commit percentage for a given user
    commit_percentage = 95  # Fallback to an estimated percentage, e.g., 95%
    # You can implement any additional logic to fetch or estimate the commit percentage
    return commit_percentage



def get_total_pull_requests(username, headers):
    prs = requests.get(f'https://api.github.com/search/issues?q=type:pr+author:{username}', headers=headers).json()
    return prs['total_count']

def get_merged_pull_requests(username, headers):
    prs = requests.get(f'https://api.github.com/search/issues?q=type:pr+is:merged+author:{username}', headers=headers).json()
    return prs['total_count']

def get_total_pr_reviewed(username, headers):
    prs_reviewed = requests.get(f'https://api.github.com/search/issues?q=type:pr+reviewed-by:{username}', headers=headers).json()
    return prs_reviewed['total_count']

def get_total_issues(username, headers):
    issues = requests.get(f'https://api.github.com/search/issues?q=type:issue+author:{username}', headers=headers).json()
    return issues['total_count']

def get_total_discussions_started(username, headers):
    discussions = requests.get(f'https://api.github.com/search/issues?q=type:discussion+author:{username}', headers=headers).json()
    return discussions['total_count']

def get_total_discussions_answered(username, headers):
    discussions = requests.get(f'https://api.github.com/search/issues?q=type:discussion+commenter:{username}', headers=headers).json()
    return discussions['total_count']

def get_total_contributions(username):
    # GraphQL query to fetch contribution years
    query = """
    query ($username: String!) {
        user(login: $username) {
            contributionsCollection {
                contributionYears
            }
        }
    }
    """
    
    variables = {"username": username}
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    
    response = requests.post(GRAPHQL_URL, json={'query': query, 'variables': variables}, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch contribution years for {username}. Status Code: {response.status_code}")
        return 0
    
    try:
        data = response.json()
        contribution_years = data['data']['user']['contributionsCollection']['contributionYears']
    except KeyError:
        print("Error fetching contribution years.")
        return 0
    
    total_contributions = 0
    for year in contribution_years:
        year_query = """
        query ($username: String!, $startDate: DateTime!, $endDate: DateTime!) {
            user(login: $username) {
                contributionsCollection(from: $startDate, to: $endDate) {
                    contributionCalendar {
                        totalContributions
                    }
                }
            }
        }
        """
        year_variables = {
            "username": username,
            "startDate": f"{year}-01-01T00:00:00Z",
            "endDate": f"{year}-12-31T23:59:59Z"
        }
        
        year_response = requests.post(GRAPHQL_URL, json={'query': year_query, 'variables': year_variables}, headers=headers)
        
        if year_response.status_code == 200:
            year_data = year_response.json()
            year_contributions = year_data['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']
            total_contributions += year_contributions
    
    return total_contributions
