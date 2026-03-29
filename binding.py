'''INSTANCE method invocation:
object.method()
python internally converts it into : ClassName.method(object)

this method is called method invocation:
pyhton does thesesteps:
findes method in objects's class.
binds that methos to the object(this is why it recieves self)
call the method with the object as the argument
'''


'''SELF PARAMETER MECHANISM:
 self refers to the current instance of the class.
 it is required in instance methods
 python automatically passes the ibject when calling
 why python uses self explicitily:
 to make data attribute clear.
 to avoid hidded variables
 ti give developers full control'''

'''METHOD RESOLUTION ORDER (MRO)
MRO decides which class,s method  is called when multiple classes define the sme methodpython follows:C3 linearization Algorithm,
order of search:
the current class
parent classes from left to right
recursively all ancestors
stop when method is found'''

class Paymentgateway:
    def connect(self):
        raise   NotImplementedError("subclass must implemente connect()")
    def pay(self,amount):
        raise NotImplementedError("subclass must implement pay()")
class StripeGateway(Paymentgateway):
    def connect(self):
        print("[stripe] connecting to stripe servers...")
    def pay(self,amount):
        print(f"[stripe] processinf payment of {amount}")
        return "STRIPE_TXN-123"
class RazorpayGateway(Paymentgateway):
    def connect(self):
        print("[Razorpay] connecting to razor pay srvers...")
        return "RAZOR_TXN_987"
                                  

class Logging:
    def log(self,message):
        print(f"[LOG]{message}")
class PaymentProcessor(Logging,StripeGateway,RazorpayGateway):
    def process_payment(self,amount):
        self.log("initializing payment")
        self.connect()
        txn_id=self.pay(amount)
        self.log(f"payment succesful:{txn_id}")
        return txn_id
processor=PaymentProcessor()
processor.process_payment(499)
print(PaymentProcessor.__mro__)



'''Types  vs class/instance
1.Types in python:
in python a type defines the characterstics and behaviour of an object.
everything in python  is an object ,a nd evry object has atype that dictates what
operation can be performed on it.
   How to check: by using the built in type() function
   Built-in types: int,str,lisr,dict,are all classes themselves
Example:'''
class Demo:
    pass
d=Demo()
print(type(d)) #userd3efined type
print(type(30)) #built_in type
 
'''2.creating classes dynamically with type()
This is where the concept of types gets meta.In Python,the type() function has
two forms:
Single Argument : type(object) return the type(class) of an object.
three argument(meta class form):type(name,beses,dict) create anew class dynamicalaly at runtime

when you use the class keyword, Python,s inrerpretor is actually executing this
three argument form of type() behind the scenes.'''

def dynamic_user_init(self,name,id):
    self.name=name
    self.id=id
def dynamic_user_get_info(self):
    return f"User: {self.name}, ID:{self.id}"
class_name="DynamicUser"
base_classes=()
class_attributes={
    "version":"1.0",
    "__init__":dynamic_user_init,
    "get_info":dynamic_user_get_info,
    }
DynamicUser=type(class_name,base_classes,class_attributes)
user_instance=DynamicUser("ABC",5001)
print(f"Instance type: {type (user_instance)}")
print(f"Info:{user_instance.get_info()}")
print(f"class attribute:{DynamicUser.version}")



'''3 everything is an obj in python:







    






