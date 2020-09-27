import os
import numpy as np
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from sklearn.externals import joblib


app = Flask(__name__)
api = Api(app)

model = joblib.load('lr.model')


class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json(force=True)
        # x = posted_data['x']
        age = posted_data['age']
        # department = posted_data['department']
        gender = posted_data['gender']
        department1 = posted_data['department_Addiction Services']
        department2 = posted_data['department_General Internal Medicine']
        department3 = posted_data['department_General Surgery']
        department4 = posted_data['department_Obstetrics']
        department5 = posted_data['department_Oncology']
        department6 = posted_data['department_Palliative Care']

        # preprocess input
        # dep = (['department_Addiction Services',
        #         'department_General Internal Medicine',
        #         'department_General Surgery', 'department_Obstetrics',
        #         'department_Oncology', 'department_Palliative Care'])
        # department_num = [[0] for i in range(len(dep))]
        # idx = dep.index(department)
        # department_num[idx][0] = 1

        # if gender == 'M':
        #     gender = 0
        # else:
        #     gender = 1

        x = [[age, gender, department1, department2, department3, department4, department5, department6]]
        prediction = model.predict(x)

        return prediction

api.add_resource(MakePrediction, '/prediction')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)