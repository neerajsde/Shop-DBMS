import mysql.connector as ms
import datetime
mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='shop')
cur=mydb.cursor()
cur.execute('select * from due_bal')
fetch=cur.fetchall()
# foreign key cos_id
cid=int(input('Enter Costumer Cos_ID: '))
for cos_id in fetch:
    if cos_id[0]==cid:
        x=int(input('Choose anyone: 1. Check dues Balance. 2. Pay Balance.: '))
        if x==1:
            mycurs=mydb.cursor()
            sql=f"select register_cos.cos_name from due_bal natural join register_cos where register_cos.cos_id={cid}"
            mycurs.execute(sql)
            name=mycurs.fetchone()
            print("----------------------------------------------------------------")
            print(f"| COS-ID: {cos_id[0]} | COS-NAME: {name[0]} | BALANCED-DUE: {cos_id[1]} |")
            print("----------------------------------------------------------------")
            break
        elif x==2:
            pay=int(input('How much money will you deposit?: '))
            ubal=cos_id[1]-pay
            mycur=mydb.cursor()
            sql1=f"update due_bal set due_balance={ubal} where cos_id={cos_id[0]}"
            mycur.execute(sql1)
            mydb.commit()
            sql2=f"update credit_ac set due_balance={ubal} where id={cos_id[0]}"
            mycur.execute(sql2)
            mydb.commit()
            sql3=f"select cos_name from register_cos where cos_id={cos_id[0]}"
            mycur.execute(sql3)
            name=mycur.fetchone()
            des='Pay Amount'
            y1=datetime.datetime.now()
            year=y1.strftime("%Y")
            month=y1.strftime("%m")
            day=y1.strftime("%d")
            date=f"{year}-{month}-{day}"
            time=y1.strftime("%X")
            sql4=f"insert into pay values ({cos_id[0]},'{name[0]}','{des}',{pay},{ubal},'{date}','{time}')"
            mycur.execute(sql4)
            mydb.commit()
            print('Thankyou for Pay balance.')
            break
 
else:
    print("Costumer-id doesn't exits")

        