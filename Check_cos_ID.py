import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Neeraj@123',database='shop')
mycur=mydb.cursor()

# ask name from user
name=input('Enter your name: ')

sql=f"select * from register_cos where cos_name='{name}'"

mycur.execute(sql)
x=mycur.fetchall()
for i in x:
    print("-------------------------------------------------------------------------------------------------------------")
    print(f"| Costumer Id: {i[0]} | Costumer Name: {i[1]} | Mobile_no: {i[2]} | Address: {i[3]} | Date: {i[4]} |")
    print("-------------------------------------------------------------------------------------------------------------")

