from Config import *
import os
import pickle
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from joblib import dump, load
import requests
import random
import json
from pandas import json_normalize

def GetData(fromDate, toDate):
    url = URL_GET_DATA
    query = {'dateFrom':fromDate, 'dateTo':toDate}
    response = requests.get(url, params=query)
    #dataRecord = { 'data' : response.json()['records']}
    #dataRecord = response.json()['records']
    # dataRecord = response.json()
    # dto = '''{response.json}'''
    # print(response.json())
    #dict = json.loads(response.json())
    dtoDF = json_normalize(response.json()['records']) 
    dtoDF.to_csv('ex.csv',index=None)
    return response.json()['records']

def ProcessTraining():

    return

def GetSubData():
    csv1 = 'CL 01-23.Last.csv'
    csv2 = 'CL 12-22.Last.csv'
    csv3 = 'DX 12-22.Last.csv'
    csv4 = 'MBT 11-22.Last.csv'
    csv5 = 'MES 12-22.Last.csv'
    
    pd1 = pd.read_csv(csv1)
    pd2 = pd.read_csv(csv2)
    pd3 = pd.read_csv(csv3)
    pd4 = pd.read_csv(csv4)
    pd5 = pd.read_csv(csv5)

    pdDate1 = pd1['Date'].drop_duplicates()
    pdDate2 = pd2['Date'].drop_duplicates()
    pdDate3 = pd3['Date'].drop_duplicates()
    pdDate4 = pd4['Date'].drop_duplicates()
    pdDate5 = pd5['Date'].drop_duplicates()

    print(len(pdDate3))

    stop = False
    loop = 0
    while loop != 100:
        rand = random.choice(pdDate3).split(' ')
        rand_num = rand[0]
        rand_num = '20221123'
        print(rand_num)
        #pdClose1 = pd1[pd1['Date'] == rand]
        #pdClose2 = pd2[pd2['Date'].str.contains(rand_num)]
        pdClose3 = pd3[pd3['Date'].str.contains(rand_num)]
        #pdClose4 = pd4[pd4['Date'] == rand]
        pdClose5 = pd5[pd5['Date'].str.contains(rand_num)]

        if(len(pdClose3) > 0 and len(pdClose5) > 0):
            #sub2 = pd2['Close']
            sub3 = pd3['Close']
            #sub4 = pd4['Close']
            sub5 = pd5['Close']
            subData = pd.DataFrame(
                {
                    #'CL': sub2,
                    'DX': sub3,
                    #'MBT': sub4,
                    'MES': sub5
                }
            )
            subData.to_csv('Subdata.csv', index=None)

            break
        loop = loop + 1
        
    return

def ProcessPredictionCorr(dataRequest):
    modelCorr = load('Models/model.joblib')
    y_pred = modelCorr.predict(dataRequest)
    return y_pred[0]

# if __name__ == "__main__":
#     # colmuns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
#     # txtFile = 'CL 01-23.Last.txt'
#     # data = pd.read_csv(txtFile)
#     # data.to_csv('CL 01-23.Last.csv', columns= colmuns)
#     GetSubData()