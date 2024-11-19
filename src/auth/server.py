import jwt, datetime, os
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

@server.route("/login", methods=["POST"])
def login():
     auth = request.authorization
     if not auth:
          return "missing credentials", 401
     
     # check DB for username and password
     
