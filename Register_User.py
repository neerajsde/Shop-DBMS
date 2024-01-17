import mysql.connector, random, datetime
mydb=mysql.connector.connect(host='localhost',user='root',password='Neeraj@123',database='shop')
mycur=mydb.cursor()

# generate random user id
cid=random.randint(1,1000)

# costumer name
name=input('Enter Costumer Name: ')

# costumer Mobile No
mob_no=input('Enter Costumer Moble number: ')
if len(mob_no)==10:
    mob=mob_no
elif len(mob_no)==0:
    print('Please Enter Costumer mobile number.')
    exit()
else:
    print('Invaild Mobile number.')
    exit()

# costumer Address
addr=input('Enter Costumer Address: ')

# date
x=datetime.datetime.now()
year=x.strftime("%Y")
month=x.strftime("%m")
day=x.strftime("%d")
date=f"{year}-{month}-{day}"

# time
time=x.strftime("%X")

# sql syntax
sql=f"insert into register_cos values ({cid},'{name}','{mob}','{addr}','{date}','{time}')"

mycur.execute(sql)
mydb.commit()
print(mycur.rowcount,"Registered Costumer data.")

sql1=f"insert into due_bal(cos_id) values ({cid})"
mycur.execute(sql1)
mydb.commit()
print('Sucessfully')