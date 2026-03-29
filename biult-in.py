'''type()-->'''
def validate_price(price):
    if type(price) in [int,float]:
        print("price is",price)
    else:
        raise TypeError("invalid price type")
validate_price(1)

def validate_price(price):
    if type(price) not in [int,float]:
         raise TypeError("invalid price type")
    else:
         print("no error")
validate_price(1)


'''is-instance()-checking a particular object belongs to a particular class or
not'''
import datetime
from decimal import Decimal
def serial(value):
    if isinstance(value,datetime.datetime):
        return value.isoformat()
    if isinstance(value,Decimal):
        return float(value)
    else:
        print("NA")
print(serial(datetime.datetime.now()))
print(serial(Decimal("10.4")))
print(serial("Hello"))
print(isinstance(10,str))
    
'''3.Attribute Functions: hasattr(),getattr(),setattr(),delattr()
these functios allows dynamic attribute access:

 A.hasattr()-->(takes only two arguments)(object,name of attribute) checks if an object contains an attribue-->used in abstraction(hiding implementation details)'''
class config:
     def __init__(self):
         self.debug=True
         self.hi=None
c1=config()
if hasattr(c1,"debug"):
    print("debuggingg mode enabled")
else:
    print("attribute not found")
print(hasattr(c1,"hi"))
print(hasattr(c1,"hello"))
print("##############################")

'''B.getattr():fetches attributes dynamiccaly'''

class User:
    name="Guest"
    email="Admin"
    phone="123"
def get_user_prop(user,prop):
    return getattr(user,prop,"not available")
u=User()
print(get_user_prop(u,'name'))
print(get_user_prop(u,'email'))
print(get_user_prop(u,'phone'))



'''c.set attr():creates and modify attributes at runtime'''
class User:
    pass
data={"id":10, "name":"sathya"  , "email":"sathya@gmail.com"}
user=User()
for key,value in data.items():
    setattr(user,key,value)
print(user.name)
print(user.email)


'''d.delattr(obj,'attr')-->delete an attributr'''
class Emplooyee:
    def __init__(self):
        self.name="abc"
        self.age=24
emp=Emplooyee()
delattr(emp,"name")
#print(emp.name)
print(emp.age)
emp1=Emplooyee()
print(emp1.name)



'''dir(): for object inspection
dir(): lists all attributes,methods,and fields of an object in sorted order'''
def inspect_object(obj):
    return [attr for attr in dir(obj) if not attr.startswith("_")]
class payment:
    def authenticator(self):pass
    def charge(self):pass
    def refund(self):pass
print(inspect_object(payment()))


'''id():for object identity-->for address
id(obj):returns the memory identity of the object
used to check if two variable reference the same underlying object.'''
a=[1,2,3]
b=a
print(id(a),id(b))
print(id(a) == id(b))
print(id(a) is id(b))#different objects
###
class Logger:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
log1=Logger()
log2=Logger()
print(id(log1)==id(log2))



'''Binding and Method Invocation--->
  1.method binding concept: binding refers to how a  programming language connects a method call to the
  actuall method implementation.
  we have two types:
  A.Early Binding(static binding):
  the method to decided a compile call,
  found in languages like c++,java for static methods
  python does not use static binding for mthods

  B.late binding(dynamic binding)
  the medthod call is decided at runtime
  python uses dynamic binding for:
  instance methods
  polymorphism
  overriding in subclasses'''
 #exampple
class Notifier:
    def send(self,message):
        raise notImpletedError("subclasses must implement the send method")
class EmailNotifier(Notifier):
    def send(self,message):
        print(f"EMAIL sent:'{message}' via SMTP server.")
class SMSnotifier(Notifier):
    def send(self,message):
        print("SMS sent :'{message}' via mobile carrier.")
Notification=[EmailNotifier(),SMSnotifier()]
test_message="your order #1234 has shipped"
for notifier in Notification:
    notifier.send(test_message)






































