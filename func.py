from datetime import datetime
from write_read import read_f

dt = datetime.now()
users = {"jb@gmail.com":{"id":dt ,"name":"john" , "pass":123}}
accounts = {dt:{"account_no":1111 ,"account_name": "j business" , "acc_balance":2000}}

ans = input("login or register {r or l}: ")




if ans.lower() == "l":
    u_email = input("whats your email")
    emails = users.keys()
    if u_email in emails:
        u_pwrd  = int(input("input your password: "))
        u_details = users[u_email]
        pswrd = u_details["pass"]
        if pswrd == u_pwrd:


            name  = u_details["name"]
            id =  u_details["id"]
            acc_info = accounts[id]
            acc_details = acc_info["account_no"]
            acc_balance = acc_info["acc_balance"]
#            print(acc_info)
            print(f"***********hello {name} welcome ***********")

            print(f"\n| ACC_NAME:\t {name}")
            print(f"\n| ACC_NO:\t {acc_details}")
            print(f"\n| ACC_BALANCE:\t {acc_balance}")









