from flask import jsonify, request
from data.resonse.common_response import response
from config.connection import *
import typing


@app.route("/get-users")
def getUsers():
    try:
        cursor.execute("select * from users")
        myresult = cursor.fetchall()
        return response(data=myresult)

    except Exception as e:
        return response(statusCode=400)


@app.route("/get-user")
def getUserById():
    data = request.get_json()

    if not data:
        return jsonify("Missing body"), 400
    elif "id" not in data:
        return jsonify("Missing id"), 400

    id = data["id"]
    cursor.execute("select * from users where id = %s", (id,))
    myresult = cursor.fetchall()

    if not myresult:
        return response(data="Not found data",statusCode=200)

    else:
        return response(data=myresult)


@app.route("/delete-user", methods=["DELETE"])
def deteleUserById():
    data = request.get_json()

    if not data:
        return jsonify("Missing body"), 400
    elif "id" not in data:
        return jsonify("Missing id"), 400

    id = data["id"]

    cursor.execute("delete from users where id = %s", (id,))
    myresult = cursor.fetchall()
    db.commit()

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

    cursor.execute("insert into users (name, email) values (%s, %s)", (name, email))
    db.commit()
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

    cursor.execute(
        "UPDATE users SET name = %s, email = %s WHERE id = %s",
        (name, email, userId),
    )
    db.commit()
    return jsonify(data), 200
