from flask import Flask, Response, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import prediction

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
class getPrediction(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:
            data = request.json
            predict = prediction.predict_models_by_request(data)
            print(predict)
            html = render_template('result.html', data=predict)
            return Response(html, mimetype='text/html')

        except Exception as error:
            return {'error': error}

@app.route('/')
def index():
    return render_template('index.html')
  
api.add_resource(getPrediction,'/simulate')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)