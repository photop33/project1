import requests


###/users/

# user_id=str(input("enter id"))
# user_name=str(input("enter user name "))
# res = requests.post('http://127.0.0.1:5000/user/'+ user_id +'', json={"user_name": ""+ user_name + ""})
# if res.ok:
#     print(res.json())

user_id=str(input("enter id"))
res = requests.get('http://127.0.0.1:5000/user/'+ user_id  +'')
if res.ok:
    print(res.json())




#/users/get_user_data/

# user_id=str(input("enter id"))
# res = requests.get('http://127.0.0.1:5001/users/get_user_data/'+ user_id  +'')
# if res.ok:
#     print(res.json())
# #
