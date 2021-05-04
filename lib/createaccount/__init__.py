from lib.database import Database
from lib.utility import generate_random,encrypt_text
import json
json_data=json.loads(open("data.json","r").read())
mysqlObj = Database()
mysqlObj.host =json_data["db-host"]
mysqlObj.username =json_data["db-username"]
mysqlObj.password =json_data["db-password"]
mysqlObj.db =json_data["db-name"]
otp_valid_duration=json_data["otp-valid-duration"] #counts in hours
class CreateAccount:
    def create_me(self):
        otp_code=generate_random()
        mysqlObj.sql = """ DELETE FROM create_account_step WHERE email="{0}" """.format(self.email)
        mysqlObj.run_sql()
        mysqlObj.sql=""" INSERT create_account_step(email,password,otp_code,otp_valid_time) VALUES('{0}','{1}','{2}',ADDTIME(NOW(), "{3}:00:00")) """.format(self.email,encrypt_text(self.password),encrypt_text(otp_code),otp_valid_duration)
        mysqlObj.run_sql()
        return {"errorCode":"6000","errorText":"Step 1 is finished","data":{"otp-code":otp_code}}

    def verify_me(self):
        mysqlObj.sql = """ SELECT email from create_account_step where email="{0}" AND password="{1}"
         AND otp_code="{2}"; 
        """.format(self.email,encrypt_text(self.password),encrypt_text(self.otp_code))
        row_no=mysqlObj.run_sql()
        if(len(row_no)==1):
            mysqlObj.sql = """ SELECT email from create_account_step where email="{0}" AND password="{1}" AND otp_code="{2}" AND otp_valid_time >= NOW(); """.format(self.email, encrypt_text(self.password),encrypt_text(self.otp_code))
            row_no = mysqlObj.run_sql()
            if(len(row_no)==1):
                user_id=generate_random(7988776566)
                mysqlObj.sql = """ INSERT users(email,username,password,user_id,otp_code,otp_valid_time) VALUES("{0}","{1}","{2}","{3}","{4}",ADDTIME(NOW(),"{5}:00:00")) ;""".format(self.email, '', encrypt_text(self.password), user_id, encrypt_text(generate_random()),otp_valid_duration)
                mysqlObj.run_sql()
                mysqlObj.sql =""" INSERT profiles(email,user_id) VALUES("{0}","{1}"); """.format(self.email,user_id)
                mysqlObj.run_sql()
                mysqlObj.sql = """ DELETE FROM create_account_step WHERE email="{0}" """.format(self.email)
                mysqlObj.run_sql()
                return {"errorText": "Account verified", "errorCode": "6001"}
            return {"errorText": "OTP code is expired", "errorCode": "5006"}
        return {"errorText":"Email,Password or OTP code is not valid","errorCode":"5005"}

