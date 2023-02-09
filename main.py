from flask import Flask, Response
from flask_restful import Resource, Api
from flask import request
import json
import funcs
class HealthCheck(Resource):
    def get(self):
        return {"ok":200}


class VowelCount(Resource):
    def post(self):
        request_data = request.get_json()
        words = request_data["words"] if "words" in request_data else None
        if (words is None):
            error = {"message": "Words field is required"}
            return Response(json.dumps(error), status=400, mimetype='application/json')
        result = {}
        for word in words:
            result[word] = funcs.count_vowels(word)
        return result

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(HealthCheck, '/')
    api.add_resource(VowelCount, '/vowel_count')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
