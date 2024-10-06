# Flask Message Collection Application

This is a simple portfolio demo page that allows users to submit messages along with their names and email addresses. The messages are stored in a MySQL database.

## Features

- User can submit their name, email, and message.
- Validates email format before submission.
- Stores messages in a MySQL database.
- Displays feedback messages to the user.

## Technologies Used

- Flask
- Flask-MySQLdb
- MySQL
- HTML/CSS for front-end templates
- Regular expressions for email validation

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- MySQL Server
- pip (Python package manager)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/flask-message-collection.git
   cd flask-message-collection
2. **Create a virtual environment**
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.  **install dependencies**
   pip install Flask Flask-MySQLdb Flask-Bcrypt

4. **Set up the Database**
    Create a new database in MySQL (e.g., testdb).
    Create a table named xlogin with the following structure:

CREATE TABLE xlogin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    message TEXT NOT NULL
); 

5.**Update Database configuration**
Open the app.py file and update the MySQL connection settings:

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'testdb'

6. **Running the application**
To run the application, execute the following command:

python app.py

