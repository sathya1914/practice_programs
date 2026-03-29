'''text processing part1:
    _________________________
1.string module:
    while python basic type (str) has many built_in methods,thw string module provides additional constants an dclasses.

    key components:
          contants:collection of characters
'''
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.whitespace)
print("\"hello")
print(string.printable)

'''2. token generation:'''
import string
import secrets
def generate_secure_token(length=12):
    alphabet=string.ascii_letters+string.digits+string.punctuation
    token=''.join(secrets.choice(alphabet) for i in range(length))
    return token
print(f"API token :{generate_secure_token()}")

'''3.string methods:
commonly used methods for data cleaning:
.strip():removes leading/trailing white space.
.split(separator):breaks a string into a list based on the delimeter.
.join(iterable):merges a list of string into one string
.relpace(old,new):swaps substring
.startwith()/endwith():checks the beginning or ending of the string

example:'''
log_entry="2023-10-27 10:00:01| ERROR |192.168.1.50|Connection Timeout"
clean_log=log_entry.strip()
parts=clean_log.split("|")
timestamp=parts[0]
level=parts[1]
message=parts[3]
if level==" ERROR ":
    print(f"Alert at {timestamp}:{message}")


'''4.String formatting:
      Method          Syntax                    Notes
     old Style(%)   "%s" %var         Legacy avoid in new code
     .format()      "{}".format(var)  Flexible good for complex templates
     f-strings      f"{var}"          Recommmended,Fastest and easiest'''

################################################
#text processing part 2
'''
1.re module(regular expression):

    the re module provides a set of funxtions that allows you to seacrh a string for a match.It uses a syntax that defines
    a "search pattern"

    Symbol    Meaning                              Example          Matches

    .       any character except new line           a.b            axb,a|b
    ^      start of string                         ^Hello          Hello
    $      end of string                            world$         world
    *       Zero or more                           ca*t            ct,cat,caat
    +      One or more                             ca+t            cat,caat
    ?      Zero or more                           colou?r          color,colour
    \d        digits(0-9)                         \d{3}            123
    \w          alphanumeric +_                   \w+               python_3
    \s        whitespaces                          \s+             spaces,tabs'''


'''2.pattern matching:

pattren matching involves defining a template (regex) and checkinng if a string conform to it.
common use casrd:
validation: ensuring an input looks like an email or a phone number.
extraction:pulling specific data(like traction ID) from aparagraph.
substitution:redacting sensitive information (like card numbers).'''


'''3.Search and Match:
    re.match():checks for a match only at the beginning of string.
    re.search():scans through the entire string for the first location where a match occurs.
    re.findall():returns  a list of all non-overlapping matches in the string.
    re.sub():repaces one or  ore matches with a different string.
    characters classes:Character classes allow matching one character from aset.
    keyRule:[^] negation,^[]starting of the string
    Common Variants:
    [a-zA-z]  #any letter
    [a-zA-z0-9] #alphanumeic
    [^a-zA-z] #not a alphabet
    [abc]   # aor b or c'''

'''example:cleanig phone number'''
import re
phone="+91-98765-43210"
cleaned=re.sub(r'[^0-9]','',phone)
print(cleaned)

'''Quantifiers{}

Quantifiers control how many times a pattern may repeat.

Quantifiers        Meaning
{n}              Exactly n times
{n,}            At least n times
{n,m}          Between n and m times
'''

'''example:[a-zA-Z]{2,4}'''
import re
pattern=r'^\d{4}$'
print(bool(re.match(pattern,"1234")))
print(bool(re.match(pattern,"123")))
print(bool(re.match(pattern,"12345")))

p1=r'^.{8}$'
print(bool(re.match(p1,"password")))
print(bool(re.match(p1,"pass")))
print(bool(re.match(p1,"password899")))

pattern2=r'^[a-zA-z]{2,4}$'
test=["In","USA","India","123","ABCabc"]
for i in test:
    print(i,bool(re.match(pattern2,i)))


'''grouping and capturing:
    parenthesis() group patterns and capture '''


import re
pattern=r'(\d{4})-(\d{4})-(\d{4})'
text="Account:1234-5678-1478,Account 1234-5678-1875"
match=re.search(pattern,text)
print(match.groups())

'''date and time module:
1.date object(datetime module):
in python standard library,the date class(found within the datetime module) represents an idealized date(year,month,day)in the georgian calendar.
common attributes: .year, .month ,.day

'''
from datetime import date
joining_date=date(2023,5,15)
today=date.today()
years_of_service=today.year-joining_date.year
print(years_of_service)


'''2.time module:
the time module is more "low-level".  it is primiraily used for intreracting with the operaating systems's clock.
key function:'''
#example 1:
import time
print(time.time())
timestamp=time.time()
print(timestamp)
print(time.ctime(timestamp))

#exaple 2:
import time
start=time.time()
print("processing data")
time.sleep(10)
end=time.time()
execution_time=end-start
print(f"task completd in {execution_time:.2f}seconds.")


'''3.date time module:
the datetime.datetime class combines'''

from datetime import datetime,timezone
now=datetime.now()
print(now)
utc_now=datetime.now(timezone.utc) #utc timezone
print(utc_now)

'''tome operarions(timedelta):
example:subscription expiry logic'''
from datetime import datetime,timedelta
pur_date=datetime.now()
trial_duration=timedelta(days=30,hours=12)
exp_date=pur_date+trial_duration
print(exp_date)
print(exp_date.strftime("%d-%m-%y %H:%M:%S"))
print(exp_date.strftime("%d-%B-%Y %H:%M:%S"))
print(exp_date.strftime("%d-%m-%y %H:%M:%S"))

#OS Module
'''1.os module Overview:
the os module acts as a bridge.Instead of writing specific code for windows(C:\path)
and different code for linux(/home/path),you use the Os module to write code
once that runs everywhere.
Core Responsibilities:
interacting with the file system(creating,deleting,moving file).
Managing directory structures.
Accessing system-level metadata and configurations.
Executing shell commands.
##############
2.File and directory operations:
Functions                              purpose
os.getcwd()                          Gets the current working directory
os.listdir(path)                    Returns alist of all files.folders in a directory
os.mkdir()/os.mkdirs()     creates a single or full nested directories
os.remove()/os.rmdir()    deletes a file or an empty directory
os.rename(ols,new)          renames the file or directory
'''
print("Os module:")
import os

cwd=os.getcwd()
print("Current working directory",cwd,"\n")
print("All files ")
list=os.listdir(cwd)
for names in list:
      print(names)
      #creating directories
single_dir="demoOs"
nested_dir="folder1/folder2"
'''if not os.path.exists(single_dir):
    os.mkdir(single_dir)
    os.makedirs(nested_dir)'''

#renaming directory
rename_="new_folder"
if os.path.exists(single_dir):
    os.rename(single_dir,rename_)

#creating a file
file_name="demo.txt"
with open(file_name,"w") as f:
    f.write("This file is created using os functions")
    #deleting a file
os.remove("demo.txt")

if os.path.exists("new_folder"):
    os.rmdir("new_folder")

#3.environment variables:
'''in software developmnet(especially in cloud and docker environments), sensitive information
like aPI keys and databese password should not be hardcoded.instead,they are stored in envirnmnet variables.
    os.environ:A directtory-like object contining all environment variables.
    os.getenv('key',default):the safer way to access a variable without crashing of it doesn't exist.
    '''
print("environment variables...")
import os
def conect():
    user=os.getenv('DATABASE_USER','guest_user')
    pwd=os.getenv('DATABASE_PASSWORD')
    print("Checking env variables....")
    if not pwd:
        print("ERROR:DATABASE_PASSWORD envoronment variable is not set.")
    else:
        print(f"Password found ,connecting to database:{user}")
if __name__=="__main__":
    conect()
    


#run pytho from cmd
DATABASE_USER="admin"
DATABASE_PASSWORD="secret12"
#python demo.py


#4. Path Operations:
'''Handling file paths manually with string concatenation (like path + "/" + file) is a major source of bugs. The os.path sub-module handles these nuances automatically.
Functions:
os.path.join()
os.path.abspath()
os.path.exists()
os.path.isfile() / os.path.isdir()
os.path.split()'''



'''web browser module:
1 web browser module:
the web browser module provides a high level interface that allows scripts to trigger the system's default web browser. It is cross platform, meaning it works seamlessly on windows, macos and linux by calling the underlying os commands

key characteristics:
simplicity: it requires zero configurations or external drivers(no need for chromedriver.exe)
passive control: it can open browser, but it cannot read the content of the page or interact with elements once the page is loaded.
user-centric: it is best used for tools where a human needs to see rsults, such as documentation viewers or dashboard launchers.

2 opening URL's :
the module povides three primary functions to open a web page, while they request specific behaviors (like new tab), the actual result often depends on the user's browser settings
function:                                            description 
webbrowser.openurl)                                  opens the url in the default browser, if window is already , it 
                                                     opens a new tab
 
webbrowser.open_new(url)                             req the browser to open a new window, if possible
webbrowser.open_new_tab(url)                         reqq the browser to open a new tab, if possible


3 browser control:
professional scripts often nneed more control than just opening the default. the get()function allows you to target specific browser if multiple are installed in the system

webbrowser.get(using=none):returns a controller obj for a specific browser type
common type name:"firefox","chrome","safari"
note:for this to work, the browser must be in the system's path. if it isnt, ypu must register the browser path manually using webbrowser.register()


web browser example:'''
import webbrowser

def open_in_chrome(url):
    try:
        browser = webbrowser.get('google-chrome')
        browser.open_new_tab(url)
    except webbrowser.Error:
        print("Chrome not found, opening default browser")
        webbrowser.open(url)

open_in_chrome("http://www.google.com")

#example 2
import webbrowser

def open_in_chrome(url):
    try:
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        
        webbrowser.register(
            "chrome",
            None,
            webbrowser.BackgroundBrowser(chrome_path)
        )
        
        webbrowser.get("chrome").open_new_tab(url)

    except webbrowser.Error:
        print("Chrome not found, opening default browser")
        webbrowser.open(url)

open_in_chrome("http://www.google.com")









'''Graphic with turtle -part-1
the turtle module is one of python's most unique features. it is a pre-installed "drawing board"
that alllows you to cotroll a "turtle" to create vector graphics.

2.Introduction to turtle module:
the turtle module provides a visual way to  see how code works.[when you give  a command like forward(100), you are'nt just changing a variable in memory you are seeing a physical manifestation
of that logic in canvas.

Key Features:
real-time rendering:you see the drawing as it happens.
event-driven : it can respond a keyborad clicks and mouse movements
coordinate system: it uses a standard cartesian(x,y) plan where(0,0) is dead
centre of the window


2.turtle graphic base:
to use turtle,you need to understand the relationship between screen(paper) and the
turtle(pen0
 Heading: the direction the turtle is facing (0 is east ,90 is north).
 pen state: is the pen down (drawing) or up(moving without leaving a mark).
 Attributes: you can change the turtles shape(arrow,turtle,circle),its speed, and the color of the ink'''
 
#3.Creating turtle Object:

import turtle
#1.Setuo the Screen (the window)
window=turtle.Screen()
window.bgcolor("white")
window.title("Graphics Demo")
#2.create the turtle object
architect=turtle.Turtle()
architect.shape("turtle")   #arrow,circle,classic,square,triangle
architect.color("blue")
architect.speed(3)#1(slow) 10(fast)
window.exitonclick()

#Graphic with turtle-part 1
'''1.Motion contrl (forward,backward,left,right):
motion control in turtle is relative.Commands move the turtle based on its current position
and the direction it is facing.
 forward(distance) or (fd):Move the turtle ahead.
 backward(distance) or(bk):moves the turtle in the opposite doirection it faces.
 right(angle) or (rt):rotates the turtle clockwise by X degrees
 left(angle) or (lt): rotates the turtle counter--clockwise X degrees '''



import turtle

t = turtle.Turtle()
t.speed(0)        # fastest
t.shape("turtle")

while True:
    t.circle(100)
























