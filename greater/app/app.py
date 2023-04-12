from flask import Flask, render_template, request, flash, redirect, url_for

from flask import Flask
from flask_restful import Api, Resource

# Create a Flask application for Addition
app = Flask(__name__)
api  = Api(app)

class Greater(Resource):
    def get(self, a, b, c, d):
        if(c == 0):
            a = -a
        if(d == 0):
            b = -b
        r = 0
        if(a > b):
            r = "True"
        else:
            r = "False"
        return {'result': r}

# Add the resource to the API
api.add_resource(Greater, '/greater/<float:a>/<float:b>/<int:c>/<int:d>')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5054,
        host="0.0.0.0"
    )