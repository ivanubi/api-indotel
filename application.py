from flask import Flask, request
from flask_restful import Resource, Api

from json import dumps
from flask_jsonpify import jsonify

import pymysql.cursors

import atexit

app = Flask(__name__)
api = Api(app)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

database = pymysql.connect (
    host="localhost",
    user = "ivanubi",
    passwd = "ubinas",
    db = "indotel", # Database with all the NXX phone codes from INDOTEL.
    cursorclass=pymysql.cursors.DictCursor)

class Phone_Number(Resource):
    def get(self, number):
        if (number.isdigit() and 6 <= len(str(number)) <= 10 ):
        # Get the cursor, which is used to traverse the database, line by line
            cursor = database.cursor()
            npa = number[0:3] # Numbering Plan Area
            nxx = number[3:6] # Three-digit code
            sql = "SELECT `prestadora`, `tipo`, `npa`,`nxx`,`localidad` FROM `indotel` WHERE (`npa`= " + npa + " AND `nxx`= " + nxx + " AND `tipo` != '1-809-200');"
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

api.add_resource(Phone_Number, '/phone_number/<number>') # Route.


if __name__ == '__main__':
     app.run()
