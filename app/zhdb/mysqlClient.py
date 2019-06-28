import  pymysql

class mysqlClient:
    def __init__(self,database,passwd,host='localhost',port=5000,user='root'):
        self.host=host
        self.port=port
        self.database=database
        self.user=user
        self.passwd=passwd
    def open(self):
        pass
    def close(self):
        pass
    def curd(self):
        pass
    def getAll(self):
        pass
