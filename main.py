from flask import Flask
from flask_restful import Resource, Api
class HealthCheck(Resource):
    def get(self):
        return {"ok":200}

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(HealthCheck, '/')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
