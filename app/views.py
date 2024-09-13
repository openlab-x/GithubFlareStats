from flask import render_template, request, send_file
from app.services import fetch_github_data
from app.utils import generate_stats_image
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from app import app

@app.route('/<username>')
def get_github_stats(username):
    # Fetching GitHub stats data for the user
    github_stats = fetch_github_data(username)

    # Ensuring valid default colors if parameters are missing
    bgColor = request.args.get('bgColor', '#ffffff')  # Default to white
    textColor = request.args.get('textColor', '#000000')  # Default to black
    cardColor = request.args.get('cardColor', '#1e1e1e')  # Default to dark gray
    chartColor = request.args.get('chartColor', '#ff9800')  # Default to orange
    chartTextColor = request.args.get('chartTextColor', '#ffffff')  # Default to white

    if request.args.get('response') == 'image':
        img = generate_stats_image(github_stats, bgColor, textColor, cardColor)
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    
    # Fallback to HTML rendering if not requesting image
    return render_template('stats.html',
                           username=username,
                           total_stars=github_stats['total_stars'],
                           total_commits=github_stats['total_commits'],
                           total_prs=github_stats['total_prs'],
                           merged_prs=github_stats['merged_prs'],
                           merged_pr_percentage=github_stats['merged_pr_percentage'],
                           pr_reviewed=github_stats['pr_reviewed'],
                           issues=github_stats['issues'],
                           discussions_started=github_stats['discussions_started'],
                           discussions_answered=github_stats['discussions_answered'],
                           total_followers=github_stats['total_followers'],
                           total_following=github_stats['total_following'],
                           total_contributions=github_stats['total_contributions'],
                           rating=github_stats['rating'],
                           bgColor=bgColor,
                           textColor=textColor,
                           cardColor=cardColor,
                           chartColor=chartColor,
                           chartTextColor=chartTextColor,
                           current_year=2024)

