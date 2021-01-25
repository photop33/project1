import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
conn.autocommit(True)

cursor = conn.cursor()

cursor.execute("DELETE FROM Q2PbjAC1nT.users WHERE name = 'shimon'")
cursor.execute("DELETE FROM Q2PbjAC1nT.users WHERE name = 'nofar'")

print ('success')

cursor.close()
conn.close()