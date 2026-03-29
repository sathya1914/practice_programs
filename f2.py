class Toy:
    def __new__(cls,*args,**kwargs):
        obj=super().__new__(cls)
        print("args:",args)
        print("kwargs:",kwargs)
        print(args,kwargs)
        return obj
        
    def __init__(self,name,name2,marks):
        self.name=name
        self.name2=name2
        self.marks=marks
    def play(self):
        print(f"playing with bike,withs marks={self.marks}")
    #def __del__(self):
       # print("t1 is deleted")
       
t1=Toy("bike","cycle",marks=10)
t1.play()
#del t1
print(id(t1))


#####################################

class Camera:
    def __init__(self,pixel):
        self.pixel=pixel
    def click(self):
        print("picture is clicked")
        print(self.pixel)

class Battery:
    def charge(self):
        print("charge is 80%")
class Storage:
    def memory(self):
        print("available space is 2 GB")

class Smartphone:
    def __init__(self,model,colour,price):
        self.model=model
        self.price=price
        self.colour=colour
        self.c=Camera(50)
        self.s=Storage()
        self.b=Battery()
    def play(self):
        print(f"phone features: {self.model} {self.price} {self.colour}")
    def phonebehaviour(self):
        self.c.click()
        self.s.memory()
        self.b.charge()
ph=Smartphone("realme","gold",40000)
ph.phonebehaviour()
ph.play()
    
        
