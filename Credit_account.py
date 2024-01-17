import mysql.connector as ms
import datetime,numpy
mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='shop')
cur=mydb.cursor()
cur.execute('select cos_id from Register_cos')
fetch=cur.fetchall()
# foreign key cos_id
cid=int(input('Enter Costumer Cos_ID: '))
for cos_id in fetch:
    if cos_id[0]==cid:
        n=int(input('Number of item: '))
        it=[]
        price=[]
        for i in range(n):
            item_name=input('Item Name: ')
            item_price=int(input('Item Price: '))
            item_n=float(input('Number/Weight of item: '))
            x=f"{item_name} x {item_n} : {item_price*item_n} "
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
        
        mycur=mydb.cursor()
        x1=f'select due_balance from due_bal where cos_id={cid}'
        mycur.execute(x1)
        bal=mycur.fetchone()
        due_bal=bal[0]+total
        x2=f"update due_bal set due_balance={due_bal} where cos_id={cid}"
        mycur.execute(x2)
        mydb.commit()
        x3=f"insert into credit_ac values ({cid},'{item}',{total},{due_bal},'{date}','{time}')"
        mycur.execute(x3)
        mydb.commit()
        print(mycur.rowcount,"Inserted")
        break
else:
    print("Costumer-Id does't exist.")
    
    
