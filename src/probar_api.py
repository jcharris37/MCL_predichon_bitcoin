import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "Open": 0.75,
    "High": 0.78,
    "Low": 0.72,
    "Volume": 0.65,
    "MA_7": 0.74
}

response = requests.post(url, json=data)
print(response.json())
