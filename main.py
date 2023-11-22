from flask import Flask, request, jsonify
from core.common_response import BaseResponseModel
import mysql.connector
import sys

app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_database",
    port=3307,
)

mycursor = mydb.cursor()

@app.route("/get-users")
def getUsers():
    try:
        mycursor.execute("select * from users")
        myresult = mycursor.fetchall()
        return jsonify(BaseResponseModel(data=myresult).to_json()),200
    
    except Exception as e:
        return jsonify(BaseResponseModel(data=myresult).to_json()),400


# @app.route("/get-user")
# def getUserById():
#     data = request.get_json()

#     if not data:
#         return jsonify("Missing body"), 400
#     elif "id" not in data:
#         return jsonify("Missing id"), 400
    
#     id = data["id"]
#     mycursor.execute("select * from users where id = %s", (id,))
#     myresult = mycursor.fetchall()

#     if not myresult:
#         return jsonify("Not found data"), 200

#     else:
#         return jsonify(myresult), 200


# @app.route("/delete-user", methods=["DELETE"])
# def deteleUserById():
#     data = request.get_json()

#     if not data:
#         return jsonify("Missing body"), 400
#     elif "id" not in data:
#         return jsonify("Missing id"), 400
    
#     id = data["id"]

#     mycursor.execute("delete from users where id = %s", (id,))
#     myresult = mycursor.fetchall()
#     mydb.commit()

#     return jsonify(myresult), 200


# @app.route("/create-user", methods=["POST"])
# def createUser():
#     data = request.get_json()

#     # Check if the 'email' field exists in the JSON data
#     if not data:
#         return jsonify({"error": "Missing body"}), 400
#     elif "email" not in data:
#         return jsonify({"error": "Missing email field"}), 400
#     elif "name" not in data:
#         return jsonify({"error": "Missing name field"}), 400

#     name = data["name"]  # Access the 'name' field from the JSON data
#     email = data["email"]  # Access the 'email' field from the JSON data

#     mycursor.execute("insert into users (name, email) values (%s, %s)", (name, email))
#     mydb.commit()
#     return jsonify(data), 200


# @app.route("/update-user/<userId>", methods=["POST"])
# def updateUser(userId):
#     data = request.get_json()

#     # Check if the 'email' field exists in the JSON data
#     if not data:
#         return jsonify({"error": "Missing body"}), 400
#     elif "email" not in data:
#         return jsonify({"error": "Missing email field"}), 400
#     elif "name" not in data:
#         return jsonify({"error": "Missing name field"}), 400

#     name = data["name"]  # Access the 'name' field from the JSON data
#     email = data["email"]  # Access the 'email' field from the JSON data

#     mycursor.execute(
#         "UPDATE users SET name = %s, email = %s WHERE id = %s",
#         (name, email, userId),
#     )
#     mydb.commit()
#     return jsonify(data), 200

# @app.route("/register", methods=["POST"])
# def register():
    # data = request.get_json()
    
    # if not data:
    return common_response.success_response(message="Success", data={"key": "value"})

if __name__ == "__main__":
    app.run(debug=True)
