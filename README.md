Django Social Media Application
Welcome to my Django Social Media Platform! Connect with others, share content, and explore exciting features.

Site Preview

Live Demo
Check out the live demo: Social Media Platform Demo

Features
Authentication: Securely sign up, sign in, and reset passwords.
Profiles: Explore, view, edit, and delete user profiles.
Posting: Create, edit, and delete posts. Attach images for a rich experience.
Comments: Engage with posts through comments.
Likes: Express your appreciation by liking posts and comments.
Saves: Easily find the posts you need by saving posts
Follow/Unfollow: Stay updated with others' posts.
Search: Easily find users.
Email Verification: Ensure account security.
Important

If you're unable to log in, make sure to enter your email information in the .env file.

Repository
Explore the source code and contribute to the development on GitHub:

GitHub Repo

Installation
Follow these steps to set up the Social Media Platform on your local machine:

Clone the repository:https://github.com/vishnu915/social_platform-DevelopersArens-month-2.git

git clone 
Install dependencies:

pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory.
Define the following environment variables:
EMAIL: Your Gmail email address for sending verification emails.
PASSWORD: Your Gmail password or an application-specific password for sending emails.
Apply database migrations:

python manage.py migrate
Run the development server:

python manage.py runserver
After completing these steps, you'll have the Social Media Platform up and running locally. Access it via your web browser at http://localhost:8000.

Usage
Sign Up / Sign In: Create an account or sign in.
Profile Management: Customize profile settings.
Posting Content: Share thoughts and multimedia.
Interacting with Content: Like, comment, and share.
Discovering Content: Find users and explore posts.
Account Settings: Manage security and privacy.
Contributing
Contributions welcome! Open issues or submit pull requests.

Important

When creating an account, ensure you enter a valid email address. You'll need to confirm it when logging in.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Important

If you're unable to log in, make sure to enter your email information in the .env file. Also, feel free to explore the source code and contribute to the development on GitHub.
