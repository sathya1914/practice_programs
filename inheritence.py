#Single inheritence
class Person:
    def details(self):
        print(f"age=23")
class Employee(Person):
    def details(self):
        super().details()
        print(f"working")
            
       
obj=Employee()
obj.details()
        
########################################
#single inherutence with init
class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def details(self):
        print(f"age=23")
class Employee(Person):
    def __init__(self,age,name,id):
        self.id=id
        super().__init__(name,age)
        
    def details(self):
        super().details()
        
        print(f"working")
        print(f"{self.name} {self.age} {self.id}")
            
       
obj=Employee("sathya",23,1)
obj.details()
###########################################################
#multiple inheritence
class A:
    def a(self):
        print("a")
class B(A):
    def b(self):
        print("b")
class C(B):
    def c(self):
        print("c")
        
obj=C()
obj.c()
obj.b()
obj.a()

###############################class A:
  
class A:
    def __init__(self,name):
        self.name=name
        
    def a(self):
        print("a")
        print(f"{self.name}")
class B(A):
    def __init__(self,name,id):
        self.id=id
        super().__init__(name)
    def a(self):
        super().a()
        print("b")
        print(f"{self.name}{self.id}")
        
class C(B):
    def __init__(self,name,id,age):
        self.age=age
        super().__init__(name,id)
    def a(self):
        super().a()
        print("c")
        print(f"{self.name} {self.id} {self.age}")
        
obj=C("alice",25,12)

obj.a()
#############################################################



class A:
    def a(self):
        print("a")
class B():
    def b(self):
        print("b")
class C(B,A):
    def c(self):
        print("c")
        
obj=C()
obj.c()
obj.b()
obj.a()


#########################################
#hierarchical
class Person:
    def details_p(self):
        print("person")
class Student(Person):
    def details_s(self):
        print("student")
class Employee(Person):
    def details_e(self):
        print("employee")

o1=Employee()
o2=Student()
o1.details_e()
o2.details_s()
o1.details_p()
o2.details_p()
print("###############")
###################################
#hierarchical with constructur
class Person:
    def __init__(self,name):
        self.name=name
    def details(self):
        print(f"{self.name}")
class Student(Person):
    def __init__(self,age,name):
        self.age=age
        super().__init__(name)
    def details(self):
        super().details()
        print(f"{self.name}{self.age}")
class Employee(Person):
    def __init__(self,id,name):
        self.id=id
        super().__init__(name)
    def details(self):
        print("employee")
        super().details()
        print(f"{self.name} {self.id}")

o1=Employee(1,"sathya")
o2=Student(12,"sathya")
o1.details()
o2.details()


###################################3333333 HYBRID
class A:
    def a(self):
        print("a")
class B(A):
    def b(self):
        print("b")
class C(A):
    def c(self):
        print("c")
class D(B,C):
    def d(self):
        print("d")        
        
obj=D()
obj.d()

#############################################
#hybrid
class Device:
    def __init__(self,name):
        self.name=name
    def details(self):
        print(f"{self.name}")
class Phone(Device):
    def __init__(self,age,name,**kwargs):
        self.age=age
        super().__init__(name,**kwargs)
    def details(self):
        super().details()
        print(f"{self.name}{self.age}")
class Laptop(Device):
    def __init__(self,speed,name,**kwargs):
        self.speed=speed
        super().__init__(name,**kwargs)
    def details(self):
          print(f"{self.name}{self.id}")
class Smartphone(Phone,Laptop):
    def __init__(self,gb,name,age,speed):
        self.gb=gb
        super().__init__(name=name,age=age,speed=speed)
    def details(self):
        print(f"{self.name}{self.speed}{self.age}{self.gb}")
        
obj=Smartphone(128,"sathya",21,123)
obj.details()
        
        
