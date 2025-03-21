list = [3,9,1,6,2,8]


# def largest(list):
#     temp = list[0]
#     for num in list:
#         if num > temp:
#             temp = num
#     return temp

# Print numbers divisible by 3 or 5 from 1 to 20 using a for loop.
 

# for num in range(1,21):
#  if num % 3 == 0 or num % 5 == 0:
#   print(num)

# Calculate factorial of a number using a while loop


# def factorial(num):
#     res = 1
#     while num > 1:
#         res = res * num
#         num = num - 1
#     return res
#-------------------------------------

# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Sample data
# users = [
#     {"id": 1, "name": "Alice"},
#     {"id": 2, "name": "Bob"}
# ]

# # GET endpoint
# @app.route('/users', methods=['GET'])
# def get_users():
#     return jsonify(users)

# # POST endpoint
# @app.route('/users', methods=['POST'])
# def add_user():
#     new_user = request.get_json()
#     users.append(new_user)
#     return jsonify(new_user), 201

# if __name__ == '__main__':
#     app.run(debug=True)

#-------------------------
# import psycopg2

# # Database connection parameters
# DB_NAME = "your_database"
# DB_USER = "your_username"
# DB_PASSWORD = "your_password"
# DB_HOST = "localhost"  # Use '127.0.0.1' for local or a remote host
# DB_PORT = "5243"       # Default PostgreSQL port

# try:
#     # Establish connection
#     conn = psycopg2.connect(
#         dbname=DB_NAME,
#         user=DB_USER,
#         password=DB_PASSWORD,
#         host=DB_HOST,
#         port=DB_PORT
#     )
#     print("Database connected successfully")

#     # Create a cursor
#     cur = conn.cursor()

#     # Execute an SQL query
#     cur.execute("SELECT version();")

#     # Fetch and print result
#     db_version = cur.fetchone()
#     print("PostgreSQL Database Version:", db_version)

#     # Close cursor and connection
#     cur.close()
#     conn.close()
# except Exception as e:
#     print("Error connecting to database:", e)


# #--------- Creating a table and inserting the data ---------- #

# import psycopg2

# try:
#     conn = psycopg2.connect(
#         dbname="your_database",
#         user="your_username",
#         password="your_password",
#         host="localhost",
#         port="5432"
#     )
#     cur = conn.cursor()

#     # Create a table
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(100),
#             age INT
#         );
#     """)

#     # Insert data
#     cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))

#     # Commit changes
#     conn.commit()

#     print("Table created and data inserted successfully.")

#     # Close cursor and connection
#     cur.close()
#     conn.close()
# except Exception as e:
#     print("Error:", e)


# import psycopg2

# # database connection parameters

# DB_NAME="your_database",
# DB_USER="your_username",
# DB_PASSWORD="your_password"
# DB_HOST="localhost",
# DB_PORT="5243"

# try:
#     conn=psycopg2.connect(
#         db_name=DB_NAME,
#         user=DB_USER,
#         password=DB_PASSWORD,
#         host=DB_HOST,
#         pirt=DB_PORT
#     )
#     print("database connected successfully")

#     # create a cursor
#     cur=conn.cursor()

#     # execute SQL query

#     db_version=cur.fetchone()
#     print("Postgresql database version:",db_version)

#     #close cursor and connection
#     cur.close()
#     conn.close()

# except Exception as e:
#     print("Error connecting database",e)   

# ------ Fetching data from postgresql


# import psycopg2

# try:
#     conn = psycopg2.connect(
#         dbname="your_database",
#         user="your_username",
#         password="your_password",
#         host="localhost",
#         port="5432"
#     )
#     cur = conn.cursor()

#     # Fetch data
#     cur.execute("SELECT * FROM users;")
#     rows = cur.fetchall()

#     for row in rows:
#         print(row)

#     # Close cursor and connection
#     cur.close()
#     conn.close()
# except Exception as e:
#     print("Error:", e)

# from flask import Flask

# app= Flask(__name__)

# @app.route('/home')

# def home():
#     return "hello there this is my first flask app";

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask

# app= Flask(__name__)

# @app.route('/home/<name>')

# def home(name):
#     return "hello"+name


# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import *
# app = Flask(__name__)

# @app.route('/admin')
# def admin():
#     return 'admin'
# @app.route('/librarian')
# def librarian():
#     return 'librarian'
# @app.route('/student')
# def student():
#     return 'student'

# @app.route('/user/<name>')
# def user(name):
#     if name =="admin":
#         return redirect(url_for(admin))
#     if name =="librarian":
#         return redirect(url_for(librarian))
#     if name =="student":
#         return redirect(url_for(student))
    
# if __name__ == "__main__":
#     app.run(debug=True)


#------ datetime---------
import datetime 
x= datetime.datetime.now()
print(x)