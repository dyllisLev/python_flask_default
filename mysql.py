import pymysql
 
 
db = pymysql.connect(host='hmini.me', port=33306, user='egg', db='egg', password='!uK8GJf3o^fh4G', charset='utf8')
curs = db.cursor()
 
sql = "SELECT * FROM personal_info WHERE BINARY(ID) = 'MASTER' AND BINARY(PASSWORD) = 'MASTER'";
 
curs.execute(sql)
 
rows = curs.fetchall()
print(rows)
 
db.commit()
db.close()