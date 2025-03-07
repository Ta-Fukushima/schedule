from flask import Flask, render_template
import app_param
import WindyAPI
from datetime import datetime

app = Flask(__name__)

@app.route('/api/sample_windy')
def sample_windy_api():
    api_key = app_param.WINDYAPI["APIKEY"]
    windy = WindyAPI.WindyAPI(api_key)
    data = windy.get_forecast(35.68, 139.76)
    # 風速と風向を表示するコード
    for i in range(len(data['ts'])):
        wind_u = data['wind_u-surface'][i]
        wind_v = data['wind_v-surface'][i]
    
        # 風速を計算
        wind_speed = (wind_u**2 + wind_v**2)**0.5
    
        # 風向を計算（度単位）
        wind_direction = (180 / 3.14159) * (3.14159 + (wind_v / wind_u))
        
        # 波の高さを取得
        # wave_height = data.get('wave-surface', [None])[i]
        
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