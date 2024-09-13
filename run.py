import time
from flask import Flask, send_file, request
from app.services import fetch_github_data
from app.utils import generate_stats_image
from io import BytesIO
from update_readme import start_periodic_update  # Importing the periodic update function

app = Flask(__name__)

# Cache for storing user stats, keyed by username
# The value will be a dictionary with "stats" and "last_updated" timestamp
cache = {}

# Function to check if cached data is still valid
def is_cache_valid(username):
    if username in cache:
        last_updated = cache[username]["last_updated"]
        # If less than 86400 seconds have passed, cache is still valid (for testing purposes)
        return time.time() - last_updated < 86400  # Changed to 86400 seconds for testing
    return False

@app.route('/<username>')
def get_github_stats(username):
    # Checking if cached stats are valid
    if is_cache_valid(username):
        # Using cached stats
        github_stats = cache[username]["stats"]
    else:
        # Fetching fresh GitHub stats data for the user
        github_stats = fetch_github_data(username)
        if 'error' in github_stats:
            return f"Error fetching stats for {username}: {github_stats['error']}", 500
        # Updating cache with new stats and timestamp
        cache[username] = {
            "stats": github_stats,
            "last_updated": time.time()
        }

    # Getting customization parameters from the URL (for theme customization)
    bgColor = request.args.get('bgColor', '#ffffff')  # Default to white
    textColor = request.args.get('textColor', '#000000')  # Default to black
    cardColor = request.args.get('cardColor', '#1e1e1e')  # Default to dark gray
    chartColor = request.args.get('chartColor', '#ff9800')  # Default to orange
    chartTextColor = request.args.get('chartTextColor', '#ffffff')  # Default to white

    # Inject the last updated time into the stats before generating the image
    github_stats["last_updated"] = cache[username]["last_updated"]

    # Generating stats image
    img = generate_stats_image(github_stats, bgColor, textColor, cardColor)

    # Save image to a BytesIO object to serve it without saving to disk
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    start_periodic_update()  # Start the periodic update function
    app.run(debug=True)
