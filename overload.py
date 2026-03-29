'''3. Operator Overloading:
Operating overloading is the process of defining custom behaviour for standard python operators (+. -, ,*, ==, >, [], etc) when used with you custom class object. Mechanism: You implement the corresponding dunder method(e.g. _add_, for +,
for <).lt
Benefit: Allows you custom objects to be used in natural, mathematical expression, making the code intuitive and readable.


'''


class Price:
   def __init__(self,amount,currency="INR"):
      self.amount=amount
      self.currency=currency
   def _validate_currency(self,other):
      if self.currency!=other.currency:
         raise ValueError("Currency mismatch, cannot perform operation")
   def __add__(self,other):
      self._validate_currency(other)
      return Price(self.amount+other.amount, self.currency)
   def __sub__(self,other):
      self._validate_currency(other)
      return Price(self.amount-other.amount, self.currency)
   def __mul__(self,qty):
      if not isinstance(qty, (int, float)):
         raise TypeError("You can only multiply price by number")
      return Price(self.amount*qty, self.currency)
   def __lt__(self,other):
      self._validate_currency(other)
      return self.amount<other.amount
   def __str__(self):
      return f"RS.{self.amount:.2f} {self.currency}"
bp=Price(1200,"INR")
dis=Price(150,"INR")
ship=Price(50,"INR")
tp=bp+ship
print("Base + shipping=",tp)
      
fp=tp-dis
print("after discount",fp)
quantity=2
bulkprice=fp*quantity
print(f"For{quantity} items =",bulkprice)
print("is base price cheaper than final price",bp<fp)

'''other oprations
__eq__ used for "=="
__gt___ used for ">"

context manager(enter and exit):
A context manager is an object that controls resource allocation and deallocation.
It properly cleaned up  after it use,even if error occurs.

The with statement quarantees that a pair of related operations will be executed.
 The interpreter precisely maps with statement to the special methods: __enter__,__exit__.
    Mechanism:The class must implement two methods:
    1.__enter__(self):Called when executionenters the with block.It usually sets up the resource
    and return the resource object.
    2.__exit__(self,exc_type,exc_val,exc_tab):called when execution leaves the with block(weather normally or due
    to an exception).
    It handles cleanup,closing connections and supressing exceptions.

    Trigger:The with  expression as target:statement.'''

class DBConnector:
   def __init__(self,db_name):
      self.db_name=db_name
      self.connection=None
   def __enter__(self):
      print(f"[ENTER] Opening connection to {self.db_name}")
      self.connection=f"Connection object for {self.db_name}"
      return self.connection
   def __exit__(self,exc_type,exc_val,exc_tab):
      if self.connection:
         print(f"[EXIT] closing connection to {self.db_name}")
      if exc_type:
         print(f"An error occured inside the block:{exc_val}")
      return False
with DBConnector("production_db") as db:
   print("enter block is first to execute")
   print(f"Inside block:Performing query usimg{db}")
   print("exit block is last to execute")
print("context block finished")


'''5. len(), getitem(), setitem(), delitem(), Container method: contains()
The special methods are often called collection or sequence protocols.
By implementing them you allow your custom objects to act like built-in Python lists or dictionaries.
This makes your code more “Pythonic” because other developers can use familiar syntax like obj[key] or len(obj)
with your custom classes.'''


class DeviceInventory:
    def __init__(self):
        self.devices = {}

    def __len__(self):
        return len(self.devices)

    def __getitem__(self, device_id):

'''privacy in python:
1.Python Access Modifiers:
a.Public:

class A:
    def fun(self):
        print("publice function")
everything is public by default in python.

2.Protected(Coventional):
    one underscore before the name :_var
    meant for internal use,but still accessible from oustide(not enforced)

class B:
    _value=10
b=B()
print(b._value)#10
Note:This is convention,Python does not block the access.

C.Private(Name-Mangled):
    Two underscores=__var
    python applies name-mangling:_ClassName__var
    intended to prevent accidental access,not impossible to access
    block the accidental access

class C:
    __secret=123#private
c=C()
print(c.__secret)#error
print(C.__secret)#error
print(c._C__secret)#123
print(C._C__secret)#123'''

'''2.Name mangling with double underscores(__):
    when you prefix a class attribute with at least two leading underscores and at most on trailing underscore(e.g. __attribute),
    python automatically rewrites(mangeles) the name include the class name as a prefix.

    when python's interpreter sees a double underscore attribute inside a calss,it transform it using this
    formula:_Class Name__AttributeName
    '''
class BaseRecord:
    def __init__(self,system_id):
        self.__id=system_id
    def get_system_id(self):
        return self.__id
class UserAccount(BaseRecord):
    def __init__(self,system_id,badge_number):
        super().__init__(system_id)
        self.id=badge_number
    def get_badge_number(self):
        return self.id

user =UserAccount(system_id="SYS-999-ID",badge_number=5001)
print("SYS_ID:",user.get_system_id())
print("Badge_bo:",user.get_badge_number())
print(user.__dict__)
