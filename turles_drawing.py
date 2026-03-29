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

'''import turtle
#1.Setuo the Screen (the window)
window=turtle.Screen()
window.bgcolor("white")
window.title("Graphics Demo")
#2.create the turtle object
architect=turtle.Turtle()
architect.shape("turtle")   #arrow,circle,classic,square,triangle
architect.color("blue")
architect.speed(3)#1(slow) 10(fast)
window.exitonclick()'''

#Graphic with turtle-part 1
'''1.Motion contrl (forward,backward,left,right):
motion control in turtle is relative.Commands move the turtle based on its current position
and the direction it is facing.
 forward(distance) or (fd):Move the turtle ahead.
 backward(distance) or(bk):moves the turtle in the opposite doirection it faces.
 right(angle) or (rt):rotates the turtle clockwise by X degrees
 left(angle) or (lt): rotates the turtle counter--clockwise X degrees '''







