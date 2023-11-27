from flask import Flask
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_database",
    port=3307,
)

cursor = db.cursor()