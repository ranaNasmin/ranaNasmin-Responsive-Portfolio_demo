# import the necessary modules
from flask import Flask, render_template,request
from flask_mysqldb import MySQL, MySQLdb, cursors
import re

# create an isinstance for Flask 
app = Flask(__name__, template_folder='templates')
#create a secret key for your app
app.secret_key = 'one+key'

#configure mysql database
app.config['MYSQL_HOST'] =  'localhost'
app.config['MYSQL_USER'] = 'sqluser'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'testdb'

# Create a MySQL instance
mysql = MySQL(app)

# route for home page
@app.route('/')
def home():
    return render_template('index.html')

# route for collecting messsages
@app.route('/message', methods=['GET','POST'])
def message():
    # Initialise a msg string so that you can return a msg 
    content = request.form['message']
    print(content)
    msg = ''
    # check if the form fields are filled completely
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'message' in request.form:
        # Create varibles for easy use
        print('hello')
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Validate the email using regular expression
        if re.match(r'[^@]+@[^@]+\.[^@]+', email):
            # Insert the data into the database
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # Run the sql queries into the database using execute method
            cursor.execute("INSERT INTO message VALUES(NULL,%s,%s,%s)",(name, email, message))  
            # Commit the queries into the database using the commit method.
            mysql.connection.commit()
            cursor.close()
            msg = 'message sent'
        else:
            msg = "invalid email address"
    else:
        msg = 'Please fill out the form Correctly!'
    return render_template('index.html', msg = msg)

# Run the main module 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)