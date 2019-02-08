from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import pymysql.cursors
import atexit
import settings

app = Flask(__name__)
api = Api(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
database = settings.db_configure()

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

            # Check if the resulted dictionary is empty.
            # bool(results)' will be True if it has something inside.
            if (bool(results) == True):
                print(results)
                return jsonify(results)

@app.errorhandler(404)
def page_not_found(error):
    return("WRONG_URL. Use the correct format: https://apiindotel.azurewebsites.net/phone_numbers/<phone_number>")

def close_connection():
    database.close()

atexit.register( close_connection ) # Close the database after Flask is shutdown.

api.add_resource(Phone_Number, '/phone_numbers/<number>') # Route.

if __name__ == '__main__':
     app.run()
