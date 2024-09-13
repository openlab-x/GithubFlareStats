from PIL import Image, ImageDraw, ImageFont, ImageOps
import time

def adjust_icon_color(icon, background_color):
    """Adjust the icon color based on the background color."""
    if background_color.lower() in ['#1e1e1e', '#333', '#000000']:  # Dark backgrounds
        # Ensure the icon is in the correct mode before inverting
        if icon.mode == 'RGBA':
            r, g, b, a = icon.split()  # Preserve the alpha channel
            rgb_image = Image.merge('RGB', (r, g, b))
            inverted_image = ImageOps.invert(rgb_image)
            icon = Image.merge('RGBA', (inverted_image.split()[0], inverted_image.split()[1], inverted_image.split()[2], a))
        else:
            icon = ImageOps.invert(icon.convert('RGB')).convert('RGBA')
    return icon

def generate_stats_image(stats, bgColor, textColor, cardColor):
    # Create an image with dimensions 800x450
    img = Image.new('RGB', (800, 450), color=bgColor)
    draw = ImageDraw.Draw(img)

    # Load the fonts (Using default fonts here, replace with truetype as needed)
    header_font = ImageFont.truetype("app/static/fonts/Font.ttf", 32)
    text_font = ImageFont.truetype("app/static/fonts/Font.ttf", 16)

    if 'error' in stats:
        draw.text((10, 10), f"Error: {stats['error']}", font=text_font, fill='red')
        return img

    # Load icons for each stat (right now all use star.png, customize paths as you have more icons)
    star_icon = adjust_icon_color(Image.open('app/static/icons/star.png').resize((20, 20)), bgColor)
    commit_icon = adjust_icon_color(Image.open('app/static/icons/commit.png').resize((20, 20)), bgColor)
    pr_icon = adjust_icon_color(Image.open('app/static/icons/pr.png').resize((20, 20)), bgColor)
    merged_pr_icon = adjust_icon_color(Image.open('app/static/icons/pr.png').resize((20, 20)), bgColor)
    issue_icon = adjust_icon_color(Image.open('app/static/icons/issue.png').resize((20, 20)), bgColor)
    discussions_icon = adjust_icon_color(Image.open('app/static/icons/discussion.png').resize((20, 20)), bgColor)
    follower_icon = adjust_icon_color(Image.open('app/static/icons/follower.png').resize((20, 20)), bgColor)
    following_icon = adjust_icon_color(Image.open('app/static/icons/following.png').resize((20, 20)), bgColor)
    contributions_icon = adjust_icon_color(Image.open('app/static/icons/contributions.png').resize((20, 20)), bgColor)

    # Draw the card background
    card_width, card_height = 780, 440
    card_x, card_y = 10, 10
    draw.rectangle((card_x, card_y, card_x + card_width, card_y + card_height), fill=cardColor)

    # Draw the username and the stats on the image
    draw.text((card_x + 20, card_y + 20), f"{stats['username']}'s GitHub Stats", font=header_font, fill=textColor)
    
    # Place icons before each stat
    icon_y_start = card_y + 70
    spacing = 30  # Spacing between each stat

    # Column settings for alignment
    icon_x = card_x + 20
    text_x = card_x + 50
    value_x = card_x + 400  # Fixed column for all the stat values

    # Paste the icons and draw the corresponding text
    img.paste(star_icon, (icon_x, icon_y_start), star_icon)
    draw.text((text_x, icon_y_start), "Total Stars:", font=text_font, fill=textColor)
    draw.text((value_x, icon_y_start), f"{stats['total_stars']}", font=text_font, fill=textColor)
    
    img.paste(commit_icon, (icon_x, icon_y_start + spacing), commit_icon)
    draw.text((text_x, icon_y_start + spacing), "Total Commits:", font=text_font, fill=textColor)
    draw.text((value_x, icon_y_start + spacing), f"{stats['total_commits']}", font=text_font, fill=textColor)
    
    img.paste(pr_icon, (icon_x, icon_y_start + spacing * 2), pr_icon)
    draw.text((text_x, icon_y_start + spacing * 2), "Total PRs:", font=text_font, fill=textColor)
    draw.text((value_x, icon_y_start + spacing * 2), f"{stats['total_prs']}", font=text_font, fill=textColor)
    
    img.paste(merged_pr_icon, (icon_x, icon_y_start + spacing * 3), merged_pr_icon)
    draw.text((text_x, icon_y_start + spacing * 3), "Total Merged PRs:", font=text_font, fill=textColor)
    draw.text((value_x, icon_y_start + spacing * 3), f"{stats['merged_prs']}", font=text_font, fill=textColor)
    
    img.paste(issue_icon, (icon_x, icon_y_start + spacing * 4), issue_icon)
    draw.text((text_x, icon_y_start + spacing * 4), "Total Issues:", font=text_font, fill=textColor)
    draw.text((value_x, icon_y_start + spacing * 4), f"{stats['issues']}", font=text_font, fill=textColor)
    
    img.paste(discussions_icon, (icon_x, icon_y_start + spacing * 5), discussions_icon)
    draw.text((text_x, icon_y_start + spacing * 5), "Discussions Started:", font=text_font, fill=textColor)
    draw.text((value_x, icon_y_start + spacing * 5), f"{stats['discussions_started']}", font=text_font, fill=textColor)
    
    img.paste(follower_icon, (icon_x, icon_y_start + spacing * 6), follower_icon)
    draw.text((text_x, icon_y_start + spacing * 6), "Total Followers:", font=text_font, fill=textColor)
    draw.text((value_x, icon_y_start + spacing * 6), f"{stats['total_followers']}", font=text_font, fill=textColor)
    
    img.paste(following_icon, (icon_x, icon_y_start + spacing * 7), following_icon)
    draw.text((text_x, icon_y_start + spacing * 7), "Total Following:", font=text_font, fill=textColor)
    draw.text((value_x, icon_y_start + spacing * 7), f"{stats['total_following']}", font=text_font, fill=textColor)
    
    img.paste(contributions_icon, (icon_x, icon_y_start + spacing * 8), contributions_icon)
    draw.text((text_x, icon_y_start + spacing * 8), "Total Contributions:", font=text_font, fill=textColor)
    draw.text((value_x, icon_y_start + spacing * 8), f"{stats['total_contributions']}", font=text_font, fill=textColor)

    # Draw the rating inside a circle at the bottom right
    rating_x, rating_y = card_x + 600, card_y + 200
    rating_radius = 66
    draw.ellipse((rating_x - rating_radius, rating_y - rating_radius, rating_x + rating_radius, rating_y + rating_radius), fill=textColor)
    
    # Draw the rating text inside the circle
    rating_font = ImageFont.truetype("app/static/fonts/Font.ttf", 32)
    rating_text = stats['rating']
    
    # Use font.getbbox() to get the text size
    bbox = rating_font.getbbox(rating_text)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((rating_x - text_width / 2, rating_y - text_height / 2), rating_text, font=rating_font, fill=cardColor)

   # Add last updated time at the bottom of the card
    last_updated_text = f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats['last_updated']))}"
    draw.text((card_x + 266, card_y + card_height - 90), last_updated_text, font=text_font, fill=textColor)

# Add a small note to inform the user about the 24-hour update cycle (split into two lines)
    update_info_text_1 = "* Stats are updated every 24 hours automatically to prevent excessive API requests"
    update_info_text_2 = "  and to ensure that the service remains efficient and avoids hitting rate limits."

# Place the two lines of the update info text
    draw.text((card_x + 20, card_y + card_height - 46), update_info_text_1, font=text_font, fill=textColor)
    draw.text((card_x + 20, card_y + card_height - 26), update_info_text_2, font=text_font, fill=textColor)
    
    
    return img
