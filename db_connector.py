import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
cursor = conn.cursor()
conn.autocommit(True)

name_table="user"
cursor.execute("CREATE TABLE `Q2PbjAC1nT`.`"+ name_table +"` (`ID` INT UNSIGNED NOT NULL,`name` VARCHAR(50) NOT NULL,"
               "`time_column`datetime (`ID`))")
print("Ready table "+ name_table +"")
conn.commit()

