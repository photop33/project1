import requests
import pymysql
user_id= '1'#str(input("enter id"))
user_name= 'lior'#str(input("enter user name "))


res = requests.post('http://127.0.0.1:5000/user/'+ user_id +'', json={"user_name": ""+ user_name + ""})
if res.ok:
    print(res.json())



user_id='3'#str(input("enter id"))
res = requests.get('http://127.0.0.1:5000/user/'+ user_id  +'')
if res.ok:
    print(res.json())

conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
cursor = conn.cursor()
cursor.execute("SELECT name FROM Q2PbjAC1nT.users;")
for row in cursor:
    if user_name == row[0]:
        print('An ',row[0],' exists in the system')

