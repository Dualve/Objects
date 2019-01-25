class Critter(object):
    """Приветствие"""
    def talk(self):
        print("Hi")
crit = Critter()
crit.talk()

class Critter1(object):
    total = 0
    @staticmethod
    def status():
        print("Сейчас зверюшек",Critter1.total)
    def __init__(self,name):
        print("New animal was born.")
        self.name = name
        Critter1.total += 1
    def __str__(self):
        rep = "Объект класса Криттер1"
        rep += "имя: " + self.name + "\n"
        return rep
    def talk(self):
        print("\n Hi, I am your pat. My name is",self.name,"\n")
        
crit1 = Critter1("Бобик")
crit1.talk()
Critter1.status()

crit2 = Critter1("Мурзик")
crit2.talk()

crit3 = Critter1("Федя")
crit3.talk()
print(crit3.total)

print("Вывод объекта критл на экран: ")
print(crit1)
print("Неаосредсвтенный доступ к атрибуту критл.нэйм: ")
print(crit1.name)
