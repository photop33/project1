# from selenium import webdriver
# import pymysql
# import time
# c = str(input("enter name in DB"))
# driver = webdriver.Chrome("C:\\Users\\l1313\\Desktop\\chromedriver.exe")
# conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
# cursor = conn.cursor()
# user_name = cursor.execute("SELECT * FROM Q2PbjAC1nT.users;")
# for row in cursor:
#     if row[1] == c:
#         print("Success - Existing",c,"db")
#         a=str(row[0])
#         time.sleep(5)
#         driver.get("http://127.0.0.1:5001/users/get_user_data/" + a + "")
#         x = driver.find_element_by_tag_name('h1')
#         a = x.text
#         q1 = []
#         q2 = []
#         for i in a:
#             for x in [chr(v) for v in range(ord('a'), ord('z'))]:
#                 if i == x:
#                     q1.append(i)
#
#                 else:
#                      continue
#
#
#         for z in c:
#             q2.append(z)
#         if q1 == q2:
#             print("Success-web element exists :)")
#             print("Test finish")
#         else:
#             print("Test Fail!", c, "do not match web:o")
#             print()
#
