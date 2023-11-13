from src.core.connect import *


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
        "UPDATE users SET name = %s, email = %s WHERE id = %s",
        (name, email, userId),
    )
    mydb.commit()
    return jsonify(data), 200
