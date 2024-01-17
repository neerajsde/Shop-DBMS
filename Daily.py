import mysql.connector as ms
import numpy, datetime
mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='shop')

name=input('Enter Costumer-Name: ')
n=int(input('Number of item: '))
it=[]
price=[]
for i in range(n):
    item_name=input('Item Name: ')
    item_price=int(input('Item Price: '))
    item_n=float(input('Number/Weight of item: '))
    x=f"{item_name} x {item_n} : {item_price*item_n}, "
    it.append(x)
    price.append(item_price*item_n)
it1=''
for k in it:
    it1=it1+k
item=it1
total=numpy.sum(price)
y1=datetime.datetime.now()
year=y1.strftime("%Y")
month=y1.strftime("%m")
day=y1.strftime("%d")
date=f"{year}-{month}-{day}"
time=y1.strftime("%X")

sql=f"insert into daily values ('{name}','{item}',{total},'{date}','{time}')"
cur=mydb.cursor()
cur.execute(sql)
mydb.commit()
print('Sucessfully submitted.')