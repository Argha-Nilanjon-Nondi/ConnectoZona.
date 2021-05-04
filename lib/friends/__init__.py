from lib.database import Database
from lib.utility import generate_random,encrypt_text
import json
json_data=json.loads(open("data.json","r").read())
mysqlObj = Database()
mysqlObj.host =json_data["db-host"]
mysqlObj.username =json_data["db-username"]
mysqlObj.password =json_data["db-password"]
mysqlObj.db =json_data["db-name"]

class Friend:
    def __init__(self,user_id):
        self.user_id=user_id

    def get_friends(self):
        mysqlObj.sql="""SELECT DISTINCT friend_id FROM friends WHERE user_id="{user_id}"; """.format(user_id=self.user_id)
        friends=mysqlObj.run_sql()
        return {"errorCode":"6003","errorText":"Friend list is here","data":friends}

    def get_friend_requsts(self):
        mysqlObj.sql="""SELECT DISTINCT friend_id FROM requests_friends WHERE user_id="{user_id}"; """.format(user_id=self.user_id)
        friends=mysqlObj.run_sql()
        return {"errorCode":"6007","errorText":"Request friend list is here","data":friends}

    def request_friend(self,friend_id):
        mysqlObj.sql = """SELECT friend_id FROM friends WHERE user_id="{user_id}" AND friend_id="{friend_id}"; 
                        """.format(user_id=self.user_id, friend_id=friend_id)
        request = mysqlObj.run_sql()
        if (len(request) > 0):
            return {"errorText": "Already you are friends", "errorCode": "5011"}
        mysqlObj.sql = """SELECT friend_id FROM requests_friends WHERE user_id="{user_id}" AND friend_id="{friend_id}"; 
        """.format(user_id=self.user_id,friend_id=friend_id)
        request = mysqlObj.run_sql()
        if(len(request)==0):
            mysqlObj.sql = """ INSERT requests_friends(user_id,friend_id) VALUES("{user_id}","{friend_id}"); """.format(user_id=self.user_id, friend_id=friend_id)
            mysqlObj.run_sql()
            return {"errorText":"Friend requests is successfully placed","errorCode":"6004"}
        if (len(request) > 0):
            return {"errorText":"Request is already placed","errorCode":"5009"}


    def accept_friend(self,friend_id):
        mysqlObj.sql = """SELECT friend_id FROM friends WHERE user_id="{user_id}" AND friend_id="{friend_id}"; 
                """.format(user_id=self.user_id, friend_id=friend_id)
        request = mysqlObj.run_sql()
        if(len(request)>0):
            return {"errorText":"Already you are friends","errorCode":"5011"}
        mysqlObj.sql = """SELECT friend_id FROM requests_friends WHERE user_id="{user_id}" AND friend_id="{friend_id}"; 
        """.format(user_id=self.user_id,friend_id=friend_id)
        request = mysqlObj.run_sql()
        if(len(request)!=0):
            mysqlObj.sql = """ INSERT friends(user_id,friend_id) VALUES("{user_id}","{friend_id}"); 
            """.format(user_id=self.user_id, friend_id=friend_id)
            mysqlObj.run_sql()
            mysqlObj.sql = """ INSERT friends(user_id,friend_id) VALUES("{friend_id}","{user_id}"); 
                        """.format(user_id=self.user_id, friend_id=friend_id)
            mysqlObj.run_sql()
            mysqlObj.sql = """ DELETE FROM requests_friends WHERE user_id="{user_id}" AND friend_id="{friend_id}"; 
            """.format(user_id=self.user_id, friend_id=friend_id)
            mysqlObj.run_sql()
            mysqlObj.sql = """ DELETE FROM requests_friends WHERE friend_id="{user_id}" AND user_id="{friend_id}"; 
            """.format(user_id=self.user_id, friend_id=friend_id)
            mysqlObj.run_sql()
            return {"errorText":"Friend is successfully added","errorCode":"6005"}
        return {"errorText":"There is no friend with the entered friend_id","errorCode":"5010"}

    def delete_friend(self,friend_id):
        mysqlObj.sql = """SELECT friend_id FROM friends WHERE user_id="{user_id}" AND friend_id="{friend_id}"; 
        """.format(user_id=self.user_id,friend_id=friend_id)
        request = mysqlObj.run_sql()
        if(len(request)!=0):
            mysqlObj.sql = """ DELETE FROM friends WHERE user_id="{user_id}" AND friend_id="{friend_id}"; 
            """.format(user_id=self.user_id, friend_id=friend_id)
            mysqlObj.run_sql()
            mysqlObj.sql = """ DELETE FROM friends WHERE user_id="{friend_id}" AND friend_id="{user_id}"; 
            """.format(user_id=self.user_id, friend_id=friend_id)
            mysqlObj.run_sql()
            return {"errorText":"Friend is successfully unfriended","errorCode":"6006"}
        return {"errorText":"There is no friend with the entered friend_id","errorCode":"5010"}
# obj=Friend("3507317371")
# print(obj.get_friends())
