import os
import signal
from flask import Flask, request

app = Flask(__name__)
users = {}
@app.route('/user/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])

def user(user_id):
        if request.method == 'POST':
            try:
                from db_connector import insert_user
                user_name = insert_user(user_id)
                return {'user id': user_id , 'user added': user_name, 'status': 'ok'}, 200 # status code
            except:
                return {"status": "error", "reason": "idal ready exists"} ,500



        elif request.method == 'GET':
            from db_connector import get_users
            try:
                user_name=get_users(user_id)
                return {"status": "ok", 'user name': user_name  }, 200 # status code
            except:
                return {"status": "error", "reason": "idal ready exists"} ,500


        elif request.method == 'PUT':
            from db_connector import update_user
            try:
                user_name =update_user(user_id)
                return {"status": "ok", "user_updated": user_name, 'status': 'ok'}, 200
            except:
                return {"status": "error", "reason": "no such id"}, 500





        elif request.method == 'DELETE':
            from db_connector import delete_user
            try:
                user_name = delete_user(user_id)
                return {"status": "ok", "user_deleted": user_name}, 200  # status code
            except:
                return {"status": "error", "reason": "no such id"}, 500




@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)

print(get())