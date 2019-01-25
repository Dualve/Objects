class Critter(object):
    def __init__(self,name):
        print("New animal was born.")
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        if new_name == "":
            print("No")
        else:
            self.__name = new_name
            print("Agree")
    def talk(self):
        print("My name:",self.name)
crit = Critter("Bob")
crit.talk()

print(crit.name) #так как есть св-во чтения

crit.name = ""
crit.name = "Ron" #так как есть св-во перезаписи

print(crit.name)    
