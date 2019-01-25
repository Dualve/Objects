class Critter(object):
    def __init__(self,name,mood):
        print("New animal was born.")
        self.name = name
        self.__mood = mood
    def talk(self):
        print("My name is", self.name)
        print("My mood is",self.__mood,"now")
        self.__private()
    def __private(self):
        print("Private area.")
        
crit = Critter(name = "Федот", mood ="добрае")
crit.talk()
print(crit._Critter__mood)
crit._Critter__private()
