import mysql.connector as ms
import datetime, numpy, time, random
for pin in range(5):
    print("\t❤️\t💕🔹🔸Welcome to General Shop🔸🔹💕\t❤️")
    upin=int(input('Enter Password: '))
    if upin==1234:
        for choose in range(100):
            cc=input("\nChoose anyone: ↩️\n1. Daily-Cash-Costomer\n2. Credit-Customer\n3. Pay-Balance/Check-Dues-Balance\n4. Register-New-Costomer\n5. Check Costomer-ID\n6. ShowAll-Registered-Costomer\n7. Date wise check celling amount.\n>>> ")
            mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database='shop')
            # Cash counter
            if cc=='1':
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
                print('✅ Sucessfully submitted.')
                print(f"Item Name: {item}")
                print(f"Total Price: {total}")
            # Credit account
            elif cc=='2':
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
                        x4=f"select * from credit_ac where Id={cid}"
                        mycur.execute(x4)
                        y4=mycur.fetchall()
                        for z4 in y4:
                            c4=f"| Cos-ID: {z4[0]} | Item-name: {z4[1]} | Total: {z4[2]} | Dues-Balance: {z4[3]} | Date: {z4[4]} |"
                            for z5 in range(len(c4)):
                                print('-',end='')
                            print()
                            print(c4)
                            for z5 in range(len(c4)):
                                print('-',end='')
                            print()
                            
                        break
                else:
                    print("❌ Costumer-Id does't exist.")
            # Check dues Balance
            elif cc=='3':
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
                            v=f"| COS-ID: {cos_id[0]} | COS-NAME: {name[0]} | BALANCED-DUE: {cos_id[1]} |"
                            for dash in range(len(v)):
                                print('-',end='')
                            print()
                            print(v)
                            for dash in range(len(v)):
                                print('-',end='')
                            print()
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
                            print('✅ Thankyou for Pay balance.')
                            mycurs=mydb.cursor()
                            sql=f"select register_cos.cos_name from due_bal natural join register_cos where register_cos.cos_id={cid}"
                            mycurs.execute(sql)
                            name=mycurs.fetchone()
                            sql5=f"Select * from due_bal where cos_id={cid}"
                            mycurs.execute(sql5)
                            cos=mycurs.fetchone()
                            v=f"| COS-ID: {cos[0]} | COS-NAME: {name[0]} | BALANCED-DUE: {cos[1]} |"
                            for dash in range(len(v)):
                                print('-',end='')
                            print()
                            print(v)
                            for dash in range(len(v)):
                                print('-',end='')
                            print()
                            break
                
                else:
                    print("❌ Costumer-id doesn't exits")
            # shut down program
            elif cc=='exit':
                exit()
            # Register New User
            elif cc=='4':
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
                print('✅ Sucessfully Registered User')
                s=f'Select * from register_cos where cos_id={cid}'
                mycur.execute(s)
                s1=mycur.fetchone()
                sp=f"| Cos-ID: {s1[0]} | Name: {s1[1]} | Mobile No: {s1[2]} | Address: {s1[3]} | Date: {s1[4]} | Time: {s1[5]} |"
                for kl in range(len(sp)):
                    print('-',end='')
                print()
                print(sp)
                for kl in range(len(sp)):
                    print('-',end='')
                print()
                
            # Check costomer name
            elif cc=='5':
                mycur=mydb.cursor()
                # ask name from user
                name=input('Enter your name: ')
                sql=f"select * from register_cos where cos_name='{name}'"
                mycur.execute(sql)
                x=mycur.fetchall()
                for i in x:
                    ff=f"| Costumer Id: {i[0]} | Costumer Name: {i[1]} | Mobile_no: {i[2]} | Address: {i[3]} | Date: {i[4]} |"
                    for f1 in ff:
                        print('-',end='')
                    print()
                    print(ff)
                    for f1 in ff:
                        print('-',end='')
                    print()
                    break
                else:
                    print(name,"doesn't Exits")
            # Show all Registered costomer
            elif cc=='6':
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
            # check daily bases selling amount
            elif cc=='7':
                y2=datetime.datetime.now()
                year=y2.strftime("%Y")
                month=y2.strftime("%m")
                day=y2.strftime("%d")
                date1=f"{year}-{month}-{day}"
                sql6=f"select sum(total) from daily where date='{date1}'"
                curs=mydb.cursor()
                curs.execute(sql6)
                ck=curs.fetchone()
                sql7=f"select sum(amount) from pay where date='{date1}'"
                curs.execute(sql7)
                h=curs.fetchone()
                total1=ck[0]+h[0]
                xx=f"|💠 {date1} is total selling price: {total1} |💠 Cash: {ck[0]} |💠 Credit: {h[0]} |"
                for xy in range(len(xx)+3):
                    print('-',end='')
                print()
                print(xx)
                for xy in range(len(xx)+3):
                    print('-',end='')
                print()

    else:
        print('❌ Wrong Password 🕘 please Try again in ')
        def countdown(time_sec):
            while time_sec:
                mins, secs = divmod(time_sec, 60)
                tim=f"{mins:02}:{secs:02}"
                print(tim,end='\r')
                time.sleep(1)
                time_sec -= 1
            print()
        countdown(10)
else:
    print('❌ Locked user try some time latter.')