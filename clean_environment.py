import requests
try:
    res = requests.get('http://127.0.0.1:5000/stop_server')
    if res.ok:
        print(res.json())
        print("success 5000")
except:
    print("Stop-server 5000")


try:
    pic = requests.get('http://127.0.0.1:5001/stop_server')
    if pic.ok:
        print(pic.json())

except:
    print("Stop-server 5001")

