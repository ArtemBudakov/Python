import pyodbc


server_name = "DESKTOP-78ICCNU\SQLEXPRESS"
db_name = "version_9.22"

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+server_name+';'
                      'DATABASE='+db_name+';'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

filter = 'test'
sql = "select r.id as receipt, max(rl.cost) as 'cost' from receipt r inner join receipt_list rl on r.id = rl.id_receipt group by r.id"
param = f'%{filter}%'
value = cursor.execute(sql, param).fetchall()

#  cursor.execute("select id from receipt where (id_restaurant = 1) or (id_restaurant = 3)")
value = cursor.fetchval()
print(value)



for row in cursor:
    print(row)

conn.close()
