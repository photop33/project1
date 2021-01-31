from flask import Flask, request
import pymysql

app = Flask(__name__)
users = {}

@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def get_user_name(user_id):
    if request.method == 'GET':
            try:
                conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY',db='Q2PbjAC1nT')
                cursor = conn.cursor()
                cursor.execute("SELECT ID FROM Q2PbjAC1nT.users;")
                for row in cursor:
                    cc=int(user_id)
                    dd=int(row[0])
                    if cc == dd:
                       row = str(row)
                       break
                cursor.close()
                conn.close()
                return "<H1 id='user'>" + row + "</H1>",{"status": "ok", 'user name': users[user_id]}, 200

            except:
                    user_id=str(user_id)
                    print(user_id)
                    return "<H1 id='error'>" "no such user:" + user_id + "</H1>",500


import os
import signal
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'



app.run(host='127.0.0.1', debug=True, port=5001)
