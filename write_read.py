import json
from datetime import datetime

dt = str(datetime.now())
users = {"jb@gmail.com":{"id":dt ,"name":"lulu" , "pass":123}}
accounts = {dt:{"account_no":1111 ,"account_name": "j business" , "acc_balance":2000}}

def read_f(file_name):
     with open(file_name , 'w') as f:
       json.dump(users , f)
     print("write successs")



def write_f(filename):
    with open(filename , 'r') as f:
         dic2 = json.load(f)
    return dic2



