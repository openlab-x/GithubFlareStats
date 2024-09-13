import time
import threading
from app.services import fetch_github_data

# Cache for storing user stats, keyed by username
# The value will be a dictionary with "stats" and "last_updated" timestamp
cache = {}

# Function to check if cached data is still valid
def is_cache_valid(username):
    if username in cache:
        last_updated = cache[username]["last_updated"]
        # If less than 86400 seconds have passed, cache is still valid (for testing purposes for testing 5 min/300 s)
        return time.time() - last_updated < 86400  # Changed to 86400 seconds for testing
    return False

# Function to update cache for a specific username
def update_cache(username):
    # Fetch fresh GitHub stats data for the user
    github_stats = fetch_github_data(username)
    if 'error' not in github_stats:
        cache[username] = {
            "stats": github_stats,
            "last_updated": time.time()
        }
    return github_stats

# Periodically update the cache every 86400 seconds (for testing 5 min/300 s) in the background
def periodic_update():
    while True:
        for username in cache.keys():
            github_stats = fetch_github_data(username)
            if 'error' not in github_stats:
                cache[username] = {
                    "stats": github_stats,
                    "last_updated": time.time()
                }
        time.sleep(86400)  # Wait for 86400 seconds (for testing 5 min/300 s))

# Start the periodic cache update
def start_periodic_update():
    update_thread = threading.Thread(target=periodic_update, daemon=True)
    update_thread.start()
