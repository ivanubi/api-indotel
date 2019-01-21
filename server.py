from flask import Flask, request
from flask_restful import Resource, Api

from json import dumps
from flask_jsonpify import jsonify

import pymysql.cursors

import atexit

app = Flask(__name__)
api = Api(app)

database = pymysql.connect (
    host="localhost",
    user = "username",
    passwd = "password",
    db = "indotel", # Database with all the NXX phone codes from INDOTEL.
    cursorclass=pymysql.cursors.DictCursor)

class Phone_Number(Resource):
    def get(self, number):
        if (number.isdigit() and 6 <= len(str(number)) <= 10 ):
        # Get the cursor, which is used to traverse the database, line by line
            cursor = database.cursor()
            npa = number[0:3] # Numbering Plan Area
            nxx = number[3:6] # Three-digit code
            sql = "SELECT `prestadora`, `tipo`, `npa`,`nxx` FROM `indotel` WHERE (`npa`= " + npa + " AND `nxx`= " + nxx + " ); "
            query = cursor.execute(sql)
            results = cursor.fetchall()

            # Check if the result dictionary is empty.
            # bool(results)' will be True if it has something inside.
            if (bool(results) == True):
                print(results)
                return jsonify(results)

def close_connection():
    database.close()

atexit.register( close_connection ) # Close the database after Flask is shutdown.

api.add_resource(Phone_Number, '/number/<number>') # Route.


if __name__ == '__main__':
     app.run(port='5002')
