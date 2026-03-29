'''import turtle
#1.Setup the Screen (the window)
window=turtle.Screen()
window.bgcolor("white")
window.title("Graphics Demo")
#2.create the turtle object
architect=turtle.Turtle()
architect.shape("arrow")#arrow,circle,classic,square,triangle
architect.color("blue")
architect.speed(3)#1(slow) 10(fast)
#Drawing a square
for i in range(4):
    architect.forward(100)
    architect.right(90)
window.exitonclick()'''


'''import turtle
#1.Setup the Screen (the window)
window=turtle.Screen()
window.bgcolor("white")
window.title("Graphics Demo")
#2.create the turtle object
architect=turtle.Turtle()
architect.shape("arrow")#arrow,circle,classic,square,triangle
architect.color("blue")
architect.speed(3)#1(slow) 10(fast)
#Drawing a circle
architect.circle(100)
window.exitonclick()'''

'''import turtle
#1.Setup the Screen (the window)
window=turtle.Screen()
window.bgcolor("white")
window.title("Graphics Demo")
#2.create the turtle object
architect=turtle.Turtle()
architect.shape("arrow")#arrow,circle,classic,square,triangle
architect.color("blue")
architect.speed(3)#1(slow) 10(fast)
#Drawing a triangle
for i in range(3):
    architect.forward(100)
    architect.left(120)
    
window.exitonclick()'''

'''import turtle
#1.Setup the Screen (the window)
window=turtle.Screen()
window.bgcolor("white")
window.title("Graphics Demo")
#2.create the turtle object
architect=turtle.Turtle()
architect.shape("arrow")#arrow,circle,classic,square,triangle
architect.color("blue")
architect.speed(3)#1(slow) 10(fast)
#Drawing a recytangle
for i in range(2):
    architect.forward(150)
    architect.left(90)
    architect.forward(100)
    architect.left(90)
    
window.exitonclick()'''

#F.Drawing

'''import turtle
import random
def create_drawing():
    screen=turtle.Screen()
    screen.bgcolor("white")
    design=turtle.Turtle()
    design.speed(10)
    colors=["#FF5733","#33FF57","#3357FF","#F333FF","#FFFF33"]
    for i in range(36):
        design.color(random.choice(colors))
        for _ in range(4):
            design.forward(100)
            design.left(90)
        design.left(10)
    screen.exitonloop()
create_drawing()
create_drawing()'''




'''import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "blue", "green", "purple", "orange"]

while True:
    t.color(random.choice(colors))
    t.circle(100)
    t.left(15)'''


'''import turtle

t = turtle.Turtle()
t.speed(0)
t.shape("turtle")

radius = 50

while True:
    t.circle(radius)
    t.left(10)
    radius += 1'''


#
'''import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.color("#FF1493")
t.left(90)

for i in range(180):
    t.circle(120)
    t.left(1)'''

#Example:Robotic vaccum simulation
'''import turtle
screen=turtle.Screen()
screen.setup(width=600,height=400)
r=turtle.Turtle()
r.shape("circle")
r.penup()
r.goto(-200,100)
r.pensize(1)
r.pendown()
r.speed(10)
for _ in range(5):
    r.fd(400)
    r.right(90)
    r.fd(30)
    r.right(90)
    r.fd(400)
    r.setheading(270)
    r.fd(30)
    r.setheading(0)
r.fd(400)
r.penup()
r.home()
r.pendown()
r.write("Clening completed",align="center",font=("Arial",16,"bold"))
r.hideturtle()
turtle.exitonclick()'''

#Graphic with Turtle Part 3
'''Color Control:
    pencolor(color):changes the color of line
    fillcolor():changes the color used when a shape is filled
    color(pencolor,fillcolor):A shortcut ton set both at once.
    turtle.colormode(255):By default Turtle uses a scale of 0.0 to 1.0 for RGB

Accepted Formats:
    String format:"red","royalblue","darkred"
    Hex Code:"#FF3456"
    RGB Tuples:(155,120,0)
2.Fill Methods(begin_fill,end_fill,fillcolor):
    begin_fill():Tells python to start tracking the coordinates of the lines you want to color.
    end_fill():end the color filling'''

'''import turtle
r=turtle.Turtle()
r.pensize(3)
r.speed(7)
r.fillcolor("red")
r.begin_fill()
r.circle(40)
r.end_fill()
r.penup()
r.fillcolor("orange")
r.begin_fill()
r.goto(100,0)
r.pendown()
r.circle(40)
r.end_fill()
r.penup()
r.goto(200,0)
r.fillcolor("green")
r.begin_fill()
r.pendown()
r.circle(40)
r.end_fill()
r.hideturtle()
turtle.exitonclick()'''

#Graphics with Turtle Part-4
'''1.Creating Multiple Turtle Objects:
    In turtle which turtle is an independemt object with:
        Its own position'''
import turtle
t1=turtle.Turtle()
t1.color("blue")
t1.shape("turtle")
t2=turtle.Turtle()
t2.color("red")
t2.shape("circle")
t3=turtle.Turtle()
t3.color("green")
t3.shape("arrow")
t1.forward(100)
t2.left(90)
t2.fd(100)
t3.penup()
t3.penup()
t3.fd(100)
t3.pendown()
t3.setheading(90)
t3.left(45)
t3.fd(150)
turtle.exitonclick()

#2.Managing Multiple Turtles:
import turtle
import random
turtles=[]
for i in range(5):
    t=turtle.Turtle()
    t.shape("circle")
    t.color(random.choice(["red","green","yellow","blue"]))
    t.penup()
    t.goto(random.randint(-200,200),random.randint(-200,200))
    t.pendown()
    t.fd(50)
    turtles.append(t)
turtle.exitonclick()

#reset and clear
''' features                 clear()                     reset()
clears drawing            yes                          yes
moves to (0,0)            no                            yes
resets direction            no                           yes
resets pen/color          no                              yes
game restart                 no                              yes'''
