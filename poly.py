## 🦆 Polymorphism  Example

class Square:
    # A standard initializer method is _init_
    def __init__(self, a):
        self.a = a
        
    def details(self): 
        area = self.a * self.a
        print(f"Area of square: {area}")

class Circle:
    def __init__(self, r):
        self.r = r
        
    def details(self):
        area = 3.14 * self.r * self.r
        print(f"Area of circle: {area}")

class  Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
        
    def details(self):
        area = self.l * self.b
        print(f"Area of rectangle: {area}")


obj = [Rectangle(2,5), Circle(10), Square(3)]


for s in obj:
    s.details()



###################################### ADDTION

class arithemetic:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        a=self.a+other.a
        b=self.b+other.b
        c=arithemetic(a,b)
        return c
o1=arithemetic(5,5)
o2=arithemetic(4,5)
o3=o1+o2
print(o3.a)
print(o3.b)


##################################METHOD OVERLOADING (with classes)
class A:
    def values(self,a,b):
        print(f"a={a} b={b}")
        
class B:
    def values(self,c,d):
       print(f"a={c} b={c}")  
        
obj1=A()
obj2=B()
obj1.values(1,2)
obj2.values(1.1,2.2)

###############################################
class Authenticator:
    def login(self,*args):
        #case1:username+password
        if len(args)==2 and isinstance(args[0],str) and isinstance(args[1],str):
            username,password=args
            return self.login_with_password(username,password)
        #case2: id+pin
        if len(args)==2 and isinstance(args[0],int) and isinstance(args[1],int):
            username,pin=args
            return self.login_with_pin(username,pin)
        #case3: faceid
        if len(args)==1 and isinstance(args[0],bytes):
            face_id=args[0]
            return self.login_with_face_id(face_id)
    def login_with_password(self,username,password):
        print("standard login succesfull")
    def login_with_pin(self,username,pin):
        print("login with pin is succes full")
    def login_with_face_id(self,face_id):
        print("login with face id is succesfull")
obj=Authenticator()
obj.login(b"sathya")
obj.login("sathya","good")
obj.login(123,456)
    
        







