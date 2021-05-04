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
class Login:
    def step_one(self):
        mysqlObj.sql = """ SELECT email from users where email="{0}" AND password="{1}";
                """.format(self.email, encrypt_text(self.password))
        row_no = mysqlObj.run_sql()
        if(len(row_no)==0):
            return {"errorCode":"5007","errorText":"Email or password is incorrect"}
        otp_code=generate_random()
        mysqlObj.sql=""" UPDATE users SET otp_valid_time=ADDTIME(NOW(),"{0}:00:00") ,otp_code="{1}" 
         WHERE email="{2}";
        """.format(otp_valid_duration,encrypt_text(otp_code),self.email)
        mysqlObj.run_sql()
        return {"errorCode":"6000","errorText":"Step 1 is finished","data":{"otp-code":otp_code}}

    def step_two(self):
        mysqlObj.sql = """ SELECT email from users where email="{0}" AND password="{1}"
         AND otp_code="{2}";
        """.format(self.email,encrypt_text(self.password),encrypt_text(self.otp_code))
        row_no=mysqlObj.run_sql()
        if(len(row_no)==1):
            mysqlObj.sql = """ SELECT email from users where email="{0}" AND password="{1}" AND otp_code="{2}" AND otp_valid_time >= NOW(); """.format(self.email, encrypt_text(self.password),encrypt_text(self.otp_code))
            row_no = mysqlObj.run_sql()
            if(len(row_no)==1):
                api_key=encrypt_text(generate_random())
                mysqlObj.sql = """ UPDATE users SET api_key="{api_key}" WHERE email="{email}";""".format(api_key=api_key,email=self.email)
                mysqlObj.run_sql()
                return {"errorText": "Login sucessfully", "errorCode": "6002","data":{"api-key":api_key}}
            return {"errorText": "OTP code is expired", "errorCode": "5006"}
        return {"errorText":"Email,Password or OTP code is not valid","errorCode":"5005"}