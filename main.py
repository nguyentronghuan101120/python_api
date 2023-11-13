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

# mycursor.execute(
#     "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"
# )
# sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
# val = [
#     ('John', 'huanvip2kk@gmail.com'),
#     ('John', 'huanvip2kk@gmail.com'),
#     ('John', 'huanvip2kk@gmail.com'),
#     ('John', 'huanvip2kk@gmail.com'),
#     ('John', 'huanvip2kk@gmail.com'),
#     ('John', 'huanvip2kk@gmail.com'),
#     ('John', 'huanvip2kk@gmail.com'),
# ]
# mycursor.executemany(sql, val)

# mydb.commit()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get-users")
def getUsers():
    mycursor.execute("select * from users")
    myresult = mycursor.fetchall()

    return jsonify(myresult), 200


@app.route("/get-users/<userId>")
def getUserById(userId):
    mycursor.execute("select * from users where id = %s", (userId,))
    myresult = mycursor.fetchall()

    return jsonify(myresult), 200


@app.route("/delete-user/<userId>", methods=["DELETE"])
def deteleUserById(userId):
    mycursor.execute("delete from users where id = %s", (userId,))
    myresult = mycursor.fetchall()
    mydb.commit()

    return jsonify(myresult), 200


@app.route("/create-user", methods=["POST"])
def createUser():
    data = request.get_json()

    # Check if the 'email' field exists in the JSON data
    if not data:
        return jsonify({"error": "Missing body"}), 400
    elif "email" not in data:
        return jsonify({"error": "Missing email field"}), 400
    elif "name" not in data:
        return jsonify({"error": "Missing name field"}), 400

    name = data["name"]  # Access the 'name' field from the JSON data
    email = data["email"]  # Access the 'email' field from the JSON data

    mycursor.execute("insert into users (name, email) values (%s, %s)", (name, email))
    mydb.commit()
    return jsonify(data), 200


@app.route("/update-user/<userId>", methods=["POST"])
def updateUser(userId):
    data = request.get_json()

    # Check if the 'email' field exists in the JSON data
    if not data:
        return jsonify({"error": "Missing body"}), 400
    elif "email" not in data:
        return jsonify({"error": "Missing email field"}), 400
    elif "name" not in data:
        return jsonify({"error": "Missing name field"}), 400

    name = data["name"]  # Access the 'name' field from the JSON data
    email = data["email"]  # Access the 'email' field from the JSON data

    mycursor.execute(
        "update  users set (name, email) values (%s, %s) where id = %s",
        (name, email, userId),
    )
    mydb.commit()
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
