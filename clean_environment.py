import requests
try:
    res = requests.get('http://127.0.0.1:5000/stop_server')
    if res.ok:
        print(res.json()
    res = requests.get('http://127.0.0.1:5001/stop_server')
    if res.ok:
        print(res.json()
except:
    print("Fail")