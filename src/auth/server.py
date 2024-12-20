import jwt
import datetime
import os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

# config
server.config["MySQL_HOST"] = os.environ.get("MySQL_HOST")
server.config["MySQL_USER"] = os.environ.get("MySQL_USER")
server.config["MySQL_PASSWORD"] = os.environ.get("MySQL_PASSWORD")
server.config["MySQL_DB"] = os.environ.get("MySQL_DB")
server.config["MySQL_PORT"] = os.environ.get("MySQL_PORT")


@server.route("/ping", methods=["GET"])
def health_check():
    return "PONG", 200


@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401

    # check DB for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM user WHERE email=%s", (auth.username,)
    )

    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        if auth.username != email or auth.password != password:
            return "invalid credentials", 401
        else:
            return create_JWT(
                username=auth.username, secret=os.environ.get("JWT_SECRET"), authz=True
            )
    else:
        return "invalid credentials", 401


@server.route("/validate", methods=["POST"])
def validate():
    encoded_jwt = request.headers["Authorization"]
    if not encoded_jwt:
        return "missing credentials", 401
    encoded_jwt = encoded_jwt.split(" ")[1]
    try:
        decoded = jwt.decode(
            encoded_jwt, os.environ.get("JWT_SECRET"), algorithms=["HS256"]
        )
    except Exception:
        return "not authorized", 403
    return decoded, 200


def create_JWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
