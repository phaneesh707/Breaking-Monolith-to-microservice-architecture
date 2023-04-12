from flask import Flask, render_template, request, flash, redirect, url_for

from flask import Flask
from flask_restful import Api, Resource

# Create a Flask application for Addition
app = Flask(__name__)
api  = Api(app)

class Substraction(Resource):
    def get(self, a, b, c, d):
        if(c == 0):
            a = -a
        if(d == 0):
            b = -b
        return {'result': a-b}

# Add the resource to the API
api.add_resource(Substraction, '/sub/<float:a>/<float:b>/<int:c>/<float:d>')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5057,
        host="0.0.0.0"
    )