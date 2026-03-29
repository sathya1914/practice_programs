class BankAccount:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal

    @staticmethod
    def validateAmount(amount):
        return amount > 0

    def deposit(self, amount):
        if BankAccount.validateAmount(amount):
            self.bal += amount
            print("Deposited amount:", amount)
            print("Current balance:", self.bal)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if BankAccount.validateAmount(amount) and amount <= self.bal:
            self.bal -= amount
            print("Withdrawal amount:", amount)
            print("Current balance:", self.bal)
        else:
            print("Invalid amount or insufficient balance")
            
acc = BankAccount("Sathya", 100)
acc.deposit(200)
acc.withdraw(100)



   #############################################

#####craeate ;object


class Toy:
     def __new__(cls,*args):
         obj=super().__new__(cls)
         print("args:",args)
         print(id(obj))
         return obj
     def __init__(self,name,bike):
         self.name=name
         self.bike=bike
         print(id(self))
         print(id(self.name))
     def play(self):
         print(f"playing with {self.name}{self.bike}")
     def __del__(self):
         print("t1 is deleted")
t1=Toy("Teddy","bike")
t1.play()
print(id(t1))

print(id(t1))
#########################################


class Student:
    def __new__(cls,*args,**kwargs):
        obj=super().__new__(cls)
       
        print("args:",args)
        print("kwargs:",kwargs)
        return obj
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks
    def sports(self):
        print(f"for the games student {self.name} {self.roll} {self.marks} has selected")
    
teacher=Student("5ax","sathya",marks=100)
teacher.sports()



#################################################################

class Library:
    def __init__(self, books):
        
        self.books = books

    def search_book(self, name):
    
        if len(name) > 2:
            if name in self.books:
                print(f"Book '{name}' found in library")
            else:
                print(f"Book '{name}' not found.")
        else:
            print("Search query must be longer than 2 letters.")


library = Library(["Machine learning", "Data Structures", "Operating Systems", "DBMS Fundamentals"])

library.search_book("Machine learning")

#####################################################################
    


































