from flask import Flask, render_template, request
import app_param
import WindyAPI
from datetime import datetime
from ModelManager import RegressionModelManager
import numpy as np

app = Flask(__name__)
@app.route('/api/sample_predict_schedule', methods=['GET', 'POST'])
def sample_predict_schedule():
    # 学習モデルを読み込む
    model = RegressionModelManager(None, None)
    model.load_model(app_param.REGRESSION_MODEL_PARAM["MODEL_PATH"])
    
    # 予測するデータを読み込む（POSTリクエストから取得）
    # input_json = request.get_json()
    
    # サンプルデータ
    input_json = [
                    {
                        "wind_speed": 6.577233848,
                        "wind_direction": -33.23158015,
                        "ship_direction": 317,
                        "ship_speed": 9.7,
                        "distance": 82.93
                    },
                    {
                        "wind_speed": 2.52200895,
                        "wind_direction": -65.8902021,
                        "ship_direction": 303,
                        "ship_speed": 8.1,
                        "distance": 40.62
                    },
                    {
                        "wind_speed": 2.459773264,
                        "wind_direction": 155.8446519,
                        "ship_direction": 237,
                        "ship_speed": 15.1,
                        "distance": 955.85
                    }
                    ]
    try:
        feature_list = []
        for entry in input_json:
            feature = [
                entry['wind_speed'],
                entry['wind_direction'],
                entry['ship_direction'],
                entry['ship_speed'],
                entry['distance']
            ]
            feature_list.append(feature)

        # NumPy配列に変換
        X = np.array(feature_list)
        
        # 予測する
        prediction = model.model.predict(X)

        # 予測結果を表示する
        return prediction.tolist()
    
    except Exception as e:
        return e

@app.route('/api/sample_windy')
def sample_windy_api():
    api_key = app_param.WINDYAPI["APIKEY"]
    windy = WindyAPI.WindyAPI(api_key)
    data = windy.get_forecast(35.68, 139.76)
    print(data)
    # 風速と風向を表示するコード
    for i in range(len(data['ts'])):
        wind_u = data['wind_u-surface'][i]
        wind_v = data['wind_v-surface'][i]
    
        # 風速を計算
        wind_speed = (wind_u**2 + wind_v**2)**0.5
    
        # 風向を計算（度単位）
        wind_direction = (180 / 3.14159) * (3.14159 + (wind_v / wind_u))
        
        # # 波の高さを取得
        # wave_height = data.get('waves_height-surface', [None])[i]
        
        # タイムスタンプを表示
        timestamp = data['ts'][i]
    
        print(f"Timestamp: {timestamp}")
        print(f"Wind Speed: {wind_speed:.2f} m/s")
        print(f"Wind Direction: {wind_direction:.2f} degrees")
        # print(f"Wave Height: {wave_height} m")
        print("------")
        
    return render_template('index.html', data=data)

@app.template_filter('datetimeformat')
def datetimeformat(value):
    return datetime.utcfromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    app.run()