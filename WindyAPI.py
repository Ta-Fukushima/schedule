import requests
import certifi

# https://api.windy.com/point-forecast/docs
class WindyAPI:
    def __init__(self, api_key):
        self.url = "https://api.windy.com/api/point-forecast/v2"
        self.api_key = api_key

    def get_forecast(self, lat, lon, model='gfs', parameters=['wind', 'temp', 'waves']):
        params = {
            'lat': lat,
            'lon': lon,
            'model': model,
            'parameters': parameters,
            'key': self.api_key
        }
        # ヘッダーの設定
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # APIリクエストを送信
        response = requests.post(self.url, json=params, headers=headers, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return None