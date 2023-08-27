
# CollegeConnect: A Social Website for Meaningful Discussions

Welcome to CollegeConnect! This is a social website built using Django and PostgreSQL, designed exclusively for college students to engage in thoughtful discussions on a wide range of topics in a public topics feed similar to Twitter. With features such as post liking, commenting, friend adding, profile customization, and private messaging, CollegeConnect aims to create a vibrant and enriching online community for college students.



## Features

- Public Topics Feed: Users can create posts on various topics, fostering discussions and sharing insights within the college community.
- Post Interactions: Users can like posts to show appreciation and leave comments to engage in meaningful conversations.
- Friend Connections: Connect with fellow students by sending and accepting friend requests, expanding your network and facilitating private interactions.
- Profile Customization: Personalize your profile with a profile picture, bio, and other customizable settings.
- Private Messaging: Communicate directly with your friends through private messages, enhancing one-on-one conversations.

## Getting Started Locally
Prerequisites:
- Python 3.6 or higher
- PostgreSQL database

## Setup

Clone the repo locally
```bash
  git clone https://github.com/ashmitg/socialwebsite.git
  cd socialwebsite
```
Create a virtual environment:
```
python -m venv venv
```
Activation for windows:
```
venve\scripts\acivate
```
Activation for Linux/Mac
```
source venv/bin/activate
```
Install the required packages
```
pip install -r requirements.txt
```
Generate your secrete key
Edit the env to add a PostgreSQL database

Use a free render PostgreSQL database:
https://dashboard.render.com/new/database

For 100% locall usage an alternative is using the PostgreSQL DB locally
https://www.postgresql.org/download/

After including the information in your .env file, run the following commands
```
python manage.py migrate
python manage.py runserver
```
Congrats!, you setup the website locally!
## Authors

- [@ashmitg](https://www.github.com/ashmitg)


## License

[MIT](https://choosealicense.com/licenses/mit/)

