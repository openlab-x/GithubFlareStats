# GithubFlareStats

![GitHub Stats](logo/logo_v1.png)

## About

**GithubFlareStats** is an open-source tool designed to generate dynamic, customizable images for displaying GitHub user statistics. It supports multiple themes and allows you to embed these stats into your GitHub profile README or any other markdown-supported platform. Display stars, commits, pull requests, issues, and much more in a visually appealing format. 

## Table of Contents

- [About](#about)
- [Features](#features)
- [Live Demo and Examples:](#live-demo-and-examples)
  - [Customization](#customization)
  - [Customization](#customization)
  - [Examples URLs](#examples-urls)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)
- [Contact](#contact)

## Features

- **Display GitHub Stats**: Showcase total stars, commits, PRs, issues, discussions, followers, and contributions.
- **Customizable Themes**: Modify background, text, and card colors via URL parameters to match your profile style.
- **Embed-Friendly**: Supports markdown embedding for GitHub profile readme files and other markdown-supported platforms.
- **Responsive**: Dynamically adjusts to different screens and usage contexts.




## Live Demo and Examples:


  - **Light Mode - Live:**
  - ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/ajee10x?response=image&bgColor=%23ffffff&textColor=%23000000&cardColor=%23e1e1e1&chartColor=%23007bff&chartTextColor=black)


  - **Dark Mode - Live:**
  - ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/ajee10x?response=image&bgColor=%231e1e1e&textColor=%23f0f0f0&cardColor=%23333&chartColor=%23ff9800&chartTextColor=white)

### Customization

| Parameter | Description |
| --- | --- |
| bgColor | Background color (e.g., #ffffff) |
| textColor | Text color (e.g., #000000) |
| cardColor | Card background color (e.g., #e1e1e1) |
| chartColor | Color for chart bars (e.g., #007bff) |
| chartTextColor | Text color for chart labels (e.g., black) |


### Examples URLs

  - **Embed Light Mode Example:**
  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/ajee10x?response=image&bgColor=%23ffffff&textColor=%23000000&cardColor=%23e1e1e1&chartColor=%23007bff&chartTextColor=black)

  ```
  - **Embed Dark Mode Example:**
  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/ajee10x?response=image&bgColor=%231e1e1e&textColor=%23f0f0f0&cardColor=%23333&chartColor=%23ff9800&chartTextColor=white)
  ```


## Usage

1. Replace ajee10x with your GitHub username in the demo URL:
  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/your-username?response=image))
  ```
2. Paste this link into your README or any markdown-supported content to showcase your GitHub stats.
  ```md
    ![GitHub Stats](https://openlabx.com/githubflarestats/api/gitfs.php/your-username?response=image&bgColor=%23f0f0f0&textColor=%23000000&cardColor=%23d9e6f2&chartColor=%23007bff&chartTextColor=black))
  ```


## Technology Stack
- Backend: Python (Flask for serving the image generation)
- Frontend: HTML, CSS, JavaScript (for theme preview and demo page)
- Image Processing: Pillow (Python Imaging Library)
- Data Caching: Implemented to reduce API calls and cache images for 24 hours.
- Proxy: PHP used as a lightweight proxy to route requests and manage caching.
- Hosting: Deployed to a production-ready hosting environment.

## Contributing
 We welcome contributions! Here's how you can help:
  
  1. Give the project a STAR.
  2. Follow us on Github.
  3. Follow us on Social Media.
  4. Fork the repository.
  5. Create a new branch for your feature or bug fix.
  6. Make your changes.
  7. Submit a pull request.
  8. Please make sure to update tests as appropriate.


## Acknowledgments
- Python: The programming language used for the backend of this project.
- Pillow: For enabling image manipulation and rendering in Python.
- GitHub API: For providing the data used in generating user stats.
- Stats are updated every 24 hours automatically to prevent excessive API requests and to ensure that the service remains efficient and avoids hitting rate limits.
- All Contributors: Thanks to everyone who contributed to the project.
- OpenLabX Team: Special thanks to the team for developing and maintaining the project.

## License
This project is licensed under the [MIT license](LICENSE).

## Contact

In pursuit of innovation,  
**OpenLabX Team**

- **Website**: [https://openlabx.com](https://openlabx.com)
- **Email**: contact@openlabx.com

**Follow Us:**

- [Instagram](https://www.instagram.com/openlabx_official/)
- [X (formerly Twitter)](https://x.com/openlabx)
- [Facebook](https://www.facebook.com/openlabx/)
- [YouTube](https://www.youtube.com/@OpenLabX)
- [GitHub](https://github.com/openlab-x)
