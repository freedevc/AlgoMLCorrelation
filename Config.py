import os 

URL_GET_DATA = "http://localhost:5090/api/correlation"

STATUS_SUCCESS_API = 1
STATUS_FAIL_API = 2
STATUS_FAIL_READFILE = 3
CONTENT_INFOR_SUCCESS = 'Predict Done !!!'
CONTENT_INFOR_FAIL_LOAD_MODEL = 'Model is not existed !!!'
CONTENT_INFOR_FAIL_PREDICT = 'The data request is not existed in Database !!!'
OS_PWD = os.getcwd()

PORT = 8009