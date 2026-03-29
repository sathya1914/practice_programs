#components amd composition:
''' 1.composition design pattern
 the composition design pattern is a principle in OOP where a class is constructured from other classes by creating instances of thoses clases as attributes.
 Instead of inheriting behaviour from a parent class ,a class delegates responsible for its components.
         Definition:  Acomplex object is built by combining se veral simpler,existing objects(componets).
         Focus:It defines the structure of a system using run-time relation-ships(object holding a reference of other object)
         Advantage:this design is highly flexible.you can easily swap out componets at run timeor add new componets without modyfing the composite class.
#has a relation is possible in compostion not in inheritance
#compostion --> loose coupling (independent of each other),works at runtime,create obj at run time
#inheritence --> tight coupling (inherits all properties of parent class)'''

#example:

class Engine:
    def start(self):
        return "engine started successfully"
class Wheels:
    def rotate(self):
        return "wheels rotaing"
class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
       #composite objects
        self.engine=Engine()
        self.wheels=[Wheels() for _ in range(4)]
    def drive(self):
        engine_status=self.engine.start()
        wheel_status=self.wheels[0].rotate()
        return f"The {self.make} is driving : {engine_status} and {wheel_status}"
my_car=Car("Thar","mahindra")
print(my_car.drive())
print(my_car.engine.start())


#2.Has-A Relationship:

#3. Creating composite objects
''' a composite object is the main class that uses copostion .
the process of creating it invovles three primary steps:
  1.Identify Components:Determine which separate, specialized clase  are needd
  2. define the composite class: create the main class
  3.Initialize componets:Instantiate ths component classes inside the coposite class's __init-- method and assign them to instance attributes'''

class Logger:
    
    
    def log_info(self,message):
        return f"[info]{message}"
class DatabaseConnector:
 
    def connect(self):
        return "Connected to SQL database"
class OrderService:
    def __init__(self):
        self.logger=Logger()
        self.db_connector=DatabaseConnector()
        self_status="Initializing"
    def process_order(self,order_id):
        log_msg_1=self.logger.log_info(f"Processing order {order_id}")
        db_msg=self.db_connector.connect()
        self.status="Processing"
        log_msg_2=self.logger.log_info("Order processed succesfully")
        return f"Order service report:\n{log_msg_1}\n{db_msg}\n{log_msg_2}"
service=OrderService()
print(service.process_order(555))

#composition vs inheritance
'''has-a          ia-a
   dynamic object static object'''



