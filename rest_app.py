from flask import Flask, request
import json
import datetime

import pymysql

app = Flask(__name__)
users = {}
@app.route('/user/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])

def user(user_id):
        if request.method == 'POST':
            try:
                request_data = request.json
                user_name = request_data.get('user_name')
                users[user_id] = user_name
                conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY',db='Q2PbjAC1nT')
                conn.autocommit(True)
                cursor = conn.cursor()
                now = datetime.datetime.utcnow()
                str_now = now.date().isoformat()
                cursor.execute('INSERT INTO Q2PbjAC1nT.users (name, id, time_column) VALUES (%s,%s,%s)', (user_name, user_id, str_now))
                cursor.close()
                conn.close()
                print ("success")
                return {'user id': user_id , 'user added': user_name, 'status': 'ok'}, 200 # status code
            except:
                return {"status": "error", "reason": "idal ready exists"} ,500



        elif request.method == 'GET':
            try:
                conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Q2PbjAC1nT.users;")
                result = cursor.fetchall()
                for row in result:
                    user_id =str(user_id)
                    show =str(row[0])
                    if show == user_id:
                            user_name=row[1]
                cursor.close()
                conn.close()
                return {"status": "ok", 'user name': user_name  }, 200 # status code
            except:
                return {"status": "error", "reason": "idal ready exists"} ,500


        elif request.method == 'PUT':
            try:
               conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY',db='Q2PbjAC1nT')
               cursor = conn.cursor()
               request_data = request.json
               user_name = request_data.get('user_name')
               users[user_id] = user_name
               cursor.execute('INSERT INTO Q2PbjAC1nT.users (name) VALUES (%s)', (user_name))
               return {"status": "ok", "user_updated" :users[user_id]}, 200 # status code
            except:
                return {"status": "error", "reason": "no such id"}, 500


        elif request.method == 'DELETE':
            try:
                conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
                conn.autocommit(True)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Q2PbjAC1nT.users WHERE name = "+ user +"")
                cursor.close()
                conn.close()
                return {"status": "ok", "user_deleted": users[user_id]}, 200  # status code
            except:
                return {"status": "error", "reason": "no such id"}, 500



app.run(host='127.0.0.1', debug=True, port=5000)

