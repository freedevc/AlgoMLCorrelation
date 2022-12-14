# AlgoMLCorrelation

At first you have to install Python with version > 3.7 (Recommend 3.10 newest) and run ```pip install -r requirements.txt```

**Link to project get Data: https://drive.google.com/file/d/1rG0T13LubrDTUgjvFvCFDBRYiz8OMQwH/view?usp=sharing**

* Please unzip the project and let the folder ```publish``` have the same level with the main project and run the file ```EA.Algo.Options.TWS.ApiServer.exe``` inside folder to start the service for getting data

* Please run ```CorrelationCollectData.py``` with command: ```python CorrelationCollectData.py```
* You can change the port and host in file ```Config.py```. **Default port is: 8009**
* API to collect Data (GET): **http://127.0.0.1:8009/api/getData?fromDate=FROMDATE&toDate=TODATE**. Please replace the **FROMDATE, TODATE** by real Date Time (exp: 2022-12-06)
* API to predict (POST):  **http://127.0.0.1:8009/api/corr**
  * Data request: ```
                    {
                        "Intercept": [1],
                        "MES": [4003.75],
                        "MBT": [20310.0],
                        "DX": [106.845]
                    }
                    ```
