import mysql.connector as ms
mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='shop')
cur=mydb.cursor()
cur.execute('select * from register_cos')
x=cur.fetchall()
for i in x:
    v=f"| Cos_id {i[0]} | Name {i[1]} | Mobile no {i[2]} | Address {i[3]} |"
    for k in range(len(v)):
        print("-",end='')
    print()
    print(v)
    for k in range(len(v)):
        print("-",end='')
    print()
