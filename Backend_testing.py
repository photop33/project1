import requests
user_id= "5"
user_name= 'Shola'

res = requests.get('http://127.0.0.1:5000/user/'+ user_id +'', json={"user_name": ""+ user_name +""})
if res.ok:
    print(res.json())



res = requests.post('http://127.0.0.1:5000/user/'+ user_id  +'')
if res.ok:
    print(res.json())
    
    
    
res = requests.put('http://127.0.0.1:5000/user/'+ user_id  +'')
if res.ok:
    print(res.json())
    
    
    
    
res = requests.delete('http://127.0.0.1:5000/user/'+ user_id  +'')
if res.ok:
    print(res.json())


