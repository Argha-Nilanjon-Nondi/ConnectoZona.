from lib.validation import  Validation
from lib.database import Database
from hashlib import sha256
import random
mysqlObj = Database()
mysqlObj.host = "127.0.0.1"
mysqlObj.username = "argha_nilanjon"
mysqlObj.password = "avunix9143"
mysqlObj.db = "connnectozona"
opt_valid_duration="10" #counts in hours

def generate_random(num=100000):
    randstr=str(random.randrange(num))
    return randstr

def encrypt_text(text):
    return sha256(text.encode("utf-8")).hexdigest()


class CreateAccount:
    def create_me(self):
        otp_code=generate_random()
        mysqlObj.sql = """ DELETE FROM create_account_step WHERE email="{0}" """.format(self.email)
        mysqlObj.run_sql()
        mysqlObj.sql=""" INSERT create_account_step(email,password,otp_code,otp_valid_time) VALUES('{0}','{1}','{2}',ADDTIME(NOW(), "{3}:00:00")) """.format(self.email,encrypt_text(self.password),otp_code,opt_valid_duration)
        mysqlObj.run_sql()
        return otp_code

    def verify_me(self):
        mysqlObj.sql = """ SELECT email from create_account_step where email="{0}" AND password="{1}"
         AND otp_code="{2}"; 
        """.format(self.email,encrypt_text(self.password),self.otp_code)
        row_no=mysqlObj.run_sql()
        if(len(row_no)==1):
            mysqlObj.sql = """ SELECT email from create_account_step where email="{0}" AND password="{1}" AND otp_code="{2}" AND otp_valid_time >= NOW(); """.format(self.email, encrypt_text(self.password), self.otp_code)
            row_no = mysqlObj.run_sql()
            if(len(row_no)==1):
                mysqlObj.sql = """ DELETE FROM create_account_step WHERE email="{0}" """.format(self.email)
                mysqlObj.run_sql()
                return {"errorText": "Account verified", "errorCode": "6001"}
            return {"errorText": "OTP code is expired", "errorCode": "5006"}
        return {"errorText":"Email,Password or OTP code is not valid","errorCode":"5005"}

