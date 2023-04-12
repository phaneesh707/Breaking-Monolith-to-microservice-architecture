from flask import Flask, render_template, request, flash, redirect, url_for

from flask import Flask
from flask_restful import Api, Resource

# Create a Flask application for Addition
app = Flask(__name__)
api  = Api(app)

class Division(Resource):
    def get(self, a, b, c, d):
        if(c == 0):
            a = -a
        if(d == 0):
            b = -b
        r = 0
        try:
            r = a/b
        except:
            r = "Value of second input cannot be zero for division"
        return {'result': r}

# Add the resource to the API
api.add_resource(Division, '/div/<float:a>/<float:b>/<int:c>/<int:d>')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5052,
        host="0.0.0.0"
    )