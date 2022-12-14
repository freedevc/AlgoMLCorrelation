import flask
from flask import request, jsonify, current_app
from flask_cors import CORS
import pickle
import json
import requests
from pandas import json_normalize
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
from Config import *
from BaseController import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["ENV"] = "production"
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/home', methods=['GET'])
def home():
    return '''<h1>API IS RUNNING</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/api/getData', methods=['GET'])
def APIGetData():
  args = request.args
  fromDate = args.get("fromDate")
  toDate = args.get("toDate")
  records = GetData(fromDate, toDate)
  return jsonify(
            Status = STATUS_SUCCESS_API,
            Data = records,
            Message = CONTENT_INFOR_SUCCESS
            )

@app.route('/api/corr', methods=['POST'])
def PredictCorr():
  args = request.json
  dto = '''{dataRequest}'''
  df_r = pd.DataFrame(args)
  y_pred_api = ProcessPredictionCorr(df_r)
  print(y_pred_api)
  return jsonify(
            Status = STATUS_SUCCESS_API,
            Data = str(y_pred_api),
            Message = CONTENT_INFOR_SUCCESS
          )

if __name__ == "__main__":
    app.run(port=PORT)


