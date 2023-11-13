from flask import Flask, request, jsonify
import mysql.connector


app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_database",
    port=3307,
)


mycursor = mydb.cursor()
if __name__ == "__main__":
    app.run(debug=True)
