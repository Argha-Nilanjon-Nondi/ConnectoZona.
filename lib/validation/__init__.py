import re
from lib.database import Database
mysqlObj = Database()
mysqlObj.host = "127.0.0.1"
mysqlObj.username = "argha_nilanjon"
mysqlObj.password = "avunix9143"
mysqlObj.db = "connnectozona"
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

obj=Validation()
# print(obj.required())
# print(obj.emailValidate("@gmail.com"))
# print(obj.passwordValidate("jmnjhgjgjhhghghghj"))
# print(obj.alreadyAccountExit("pcic0095@gmail.com"))