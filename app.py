from flask import Flask
from flask_restful import Api
from resource.empresa import empresa

app = Flask(__name__)
api = Api(app)

api.add_resource(empresa, "/empresa/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)