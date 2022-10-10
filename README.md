"The Gym Buddy" Gym Management App

About The Project:

After 4 weeks of an intensive 16-week software development course at CodeClan we were tasked with creating our first full-stack application.

The brief:

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes. MVP

The app should allow the gym to create and edit Members
The app should allow the gym to create and edit Classes
The app should allow the gym to book members on specific classes
The app should show a list of all upcoming classes
The app should show all members that are booked in for a particular class

Built With:
- Python
- Flask
- HTML
- CSS
- Postgresql

Getting Started
Prerequisites
To run this app, you must have:

psychopg

pip3 install psycopg2
Flask

pip3 install Flask
Postgresql

Installation:

Clone the repo
git clone https://github.com/Johbruca/gym_app_project.git

Navigate via Terminal to the folder

Create the database

psql -d gym_app -f db/gym_app.sql

Populate the database with pre-set objects

python3 console.py

Run Flask

flask run

Open in Chrome: http://127.0.0.1:5000

To stop the server enter ctrl + c in your Terminal
