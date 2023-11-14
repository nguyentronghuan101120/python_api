from flask import jsonify


def success_response(**kwargs):
    for key, value in kwargs.items():
        return jsonify(
            {
                "statusCode": 200,
                "body": key["body"],
            },

            200
        )
