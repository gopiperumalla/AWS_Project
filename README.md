# Flask Web Application with SQLite3

This is a simple web application built using Flask and SQLite3. The app features user registration, login, and a dashboard. It is designed to run on an AWS EC2 instance using the Flask development server.

## Features

- User authentication (login, registration)
- SQLite3 database for user data storage
- Flash messages for feedback
- Session management for logged-in users
- Deployment instructions for AWS EC2 (Ubuntu)

## Prerequisites

- Python 3.x
- Flask
- SQLite3
- AWS EC2 (Ubuntu)

## Project Structure

```bash
.
├── app.py                  # Main Flask application file
├── users.db                # SQLite3 database file (auto-generated after running the app)
├── templates               # Directory containing HTML files
│   ├── login.html          # Login page template
│   ├── register.html       # Registration page template
└── README.md               # Project README file
