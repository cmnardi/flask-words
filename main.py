"""Api com funcões para manipular palavras."""
import json

from flask import Flask, Response, request
from flask_restful import Resource, Api

import funcs
class HealthCheck(Resource): # pylint: disable=too-few-public-methods
    """Testar se a api está ok."""
    def get(self):
        """Testar se a api está ok."""
        return {"ok":200}

class VowelCount(Resource): # pylint: disable=too-few-public-methods
    """Contar as vogais de cada palavra."""
    def post(self):
        """Contar as vogais de cada palavra."""
        request_data = request.get_json()
        words = request_data["words"] if "words" in request_data else None
        if words is None:
            error = {"message": "Words field is required"}
            return Response(json.dumps(error), status=400, mimetype='application/json')
        result = {}
        for word in words:
            result[word] = funcs.count_vowels(word)
        return result

class Sort(Resource): # pylint: disable=too-few-public-methods
    """Ordenar as strings passadas."""
    def post(self):
        """Ordenar as strings passadas."""
        request_data = request.get_json()
        words = request_data["words"] if "words" in request_data else None
        order = request_data["order"] if "order" in request_data else None
        errors = []
        if words is None:
            errors.append("Words field is required")
        if order is None:
            errors.append("Order field is required")
        elif (order not in ["asc", "desc"]):
            errors.append("Order field must be asc or desc")
        if errors:
            return Response(json.dumps({"errors":errors}), status=400, mimetype='application/json')
        return funcs.order(words, order)


app = Flask(__name__)
api = Api(app)
api.add_resource(HealthCheck, '/')
api.add_resource(VowelCount, '/vowel_count')
api.add_resource(Sort, '/sort')


if __name__ == '__main__':
    app.run(debug=True)
