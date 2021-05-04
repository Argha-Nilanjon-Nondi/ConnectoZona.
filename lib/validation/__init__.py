import re
from lib.database import Database
import json
json_data=json.loads(open("data.json","r").read())
mysqlObj = Database()
mysqlObj.host =json_data["db-host"]
mysqlObj.username =json_data["db-username"]
mysqlObj.password =json_data["db-password"]
mysqlObj.db =json_data["db-name"]
class Validation:
    def required(self,data=None):
        """ check if the entered string is none and empty of filled . If filled returned true aotherwise return false """
        if(data==None):
            return False
        step1=data.replace(" ","")
        if(len(step1)==0):
            return False
        return True

    def emailValidate(self,email):
        """return true if the email is valid otherwise return false"""
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if (re.search(regex, email)):
            return True
        return False

    def passwordValidate(self,password):
        """return true if the password isn"t empty and it"s length is greater than 8 """
        if(" " in password):
            return False
        step1=password.replace(" ","")
        if(len(step1)==0 or len(step1)<7):
            return False
        return True

    def alreadyAccountExist(self,email):
        mysqlObj.sql = """ SELECT email from users where email="{0}" """.format(email)
        row_no=mysqlObj.run_sql()
        if(len(row_no)>0):
            return True
        return False

    def UserIdExist(self,user_id):
        mysqlObj.sql = """ SELECT user_id from users where user_id="{0}" """.format(user_id)
        row_no = mysqlObj.run_sql()
        if (len(row_no) > 0):
            return True
        return False

    def ApiKeyExist(self,api_key):
        mysqlObj.sql = """ SELECT api_key from users where api_key="{api_key}" """.format(api_key=api_key)
        row_no = mysqlObj.run_sql()
        if (len(row_no) > 0):
            return True
        return False

    def ApiKeyToUserID(self,api_key):
        mysqlObj.sql = """ SELECT user_id from users where api_key="{api_key}" """.format(api_key=api_key)
        key = mysqlObj.run_sql()
        return key[0][0]
# obj=Validation()
# print(obj.required())
# print(obj.emailValidate("@gmail.com"))
# print(obj.passwordValidate("jmnjhgjgjhhghghghj"))
# print(obj.alreadyAccountExit("pcic0095@gmail.com"))
# print(obj.UserIdExist("pcic0095@gmail.com"))