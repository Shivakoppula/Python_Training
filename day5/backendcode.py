def display():
    for var in ['f1','f2','f3']:
        print(var)
        
class cname:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def display(self):
        return self.a, self.b
    
def connect(dsn):
    class Connection:
        def __init__(self,dsn,dbname,pasword):
            self.dsn = dsn
            self.dbname = dbname
            self.pasword = pasword
        def method1(self):
            return "query executed"
    obj=Connection(dsn,'sql','password')
    return obj
           