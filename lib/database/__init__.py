import pymysql
import json
class Database:

    def run_sql(self):
        db = pymysql.connect(host= self.host,user=self.username,password=self.password,database=self.db,port=3306)
        cursor = db.cursor()
        try:
            cursor.execute(self.sql)
            db.commit()
            result=json.loads(json.dumps(cursor.fetchall()))
            return result
        except Exception as error:
            db.rollback()
            print(error)
            return ()
        db.close()

# obj=Database()
# obj.host="127.0.0.1"
# obj.username="argha_nilanjon"
# obj.password="avunix9143"
# obj.db="connnectozona"
# obj.sql=""" SELECT * from create_account_step where email="12436@gmail.comp" """
# print(obj.run_sql())