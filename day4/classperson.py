class Person:
    def __init__(self,name):
        self.name = name

class Vendor(Person):
    def __init__(self,name,vid):
        super().__init__(name)
        self.vid = vid
    

obj  = Vendor('Klabs','V123')
print(obj.name)
print(obj.vid)