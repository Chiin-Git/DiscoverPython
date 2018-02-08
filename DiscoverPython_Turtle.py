# (Slides) AS ATTENDEES ARRIVE: SIT THEM IN CLUSTERS ACCORDING TO EXPERIENCE, CHECK TRINKET SET-UP + aged 13+ + GIVE HAND-OUTS

# (Slides) WELCOME: to the Discover Python workshop - Programming Virtual Turtles to draw Computer Graphics 
# (Slides) TWITTER

# (Slides) This workshop is for people who've never done any coding before, or who've maybe done some programmimg in another language but never in Python
# (Slides) First let's set the scene for the next hour - computer-generated graphics! Today's workshop is inspired by this photo of fireworks
# (Trinket) And this is what you'll be learning how to program over the next hour! | using a series of building block exercises

# (Trinket) Intro to you - who is in school/college/uni/working? I'm expecting everyone is new to Python? Have you done any other programming languages before?

# (Slides) Intro to me | Intro to mentors 

# (Slides) So let's just set the scene a bit and talk about Languages: first of all, let's talk about Natural Languages - English is my first language, but what's yours?
# So in the same way some of us communicate in a variety of Natural Languages to talk to different people, 
# ...people in Tech communicate in a variety of Computer Languages to talk to/work with different technologies 
# ...e.g. Computer Languages for writing instructions for robots, to make apps, 

# (Slides) But today we're doing Python! So why Python? | Python is one of the most common & useful Computer Languages in Tech - the equivalent of English as a Natural Language
# ...so if you know Python, you have the power to do lots of cool things! Amongst the mentors in the room, we've done cool things in Python, like CyberSec, Robotics, Algos
# MENTORS: share how you're using Python in your work/academic research

# We'll show more examples of Python use-cases at the end if we have enough time

# BUT now let's start Discovering Python instead of talking about it!!

# (Trinket) Access the pre-prepared programming environment - today we're using a particular way of writing & running Python - a free online platform which has all the software already installed
	#As you become more experienced with Python you'll want to set up a local programming environment i.e. on your personal computer
	#(****NOTE: anyone under 13**** | We're going to do x exercises, leading up to the Firework grahpic
	#New Trinket: see the different computer languages you can write in this environment
	#Choose Python (this runs Python 2 and 3)
	#Call it something | Save

# I WANT TO GET THROUGH EXERICSES A - L: each exercise is a BUILDING BLOCK to that final fireworks computer-generated graphic, so please try to understand what's going on

# There are 2 ways to run code ^for any language: 1. line by line in a console, 2. write a whole program which is stored in a file which then gets executed by an interpreter

#If you quit from the Python interpreter and enter it again, the definitions you have made (functions and variables) are lost. 
#Therefore, if you want to write a somewhat longer program, you are better off using a text editor to prepare the input for the interpreter and running it with that file as input instead. 
#This is known as creating a script. As your program gets longer, you may want to split it into several files for easier maintenance. 
#You may also want to use a handy function that you’ve written in several programs without copying its definition into each program.


# Exercise A: Run some Python code line by line
	# Find and click the Console button
	# Let's write some Python which uses the computer as a calculator 
	# Let's do some calculations together using Python arithmetic operators + - * / | Shout your favourite number to me 
	# range()

342 + 43298

range(5)	#Note it starts at 0, and ends at 5 not including 5

# Exercise B: Run Python code as a script | As you can see, the Console is good for simple instructions - however, most of the time you'll be writing a Python script
	# If you have a series of instructions to get to the output you want then you'll need to write multiple lines of code
	# white space is used to denote separate elements/code blocks

	# When you write a series of instructions like this, you are writing a program

	# Calculate the number of people in this room
	# In this program, we're going to be using a critical concept in Python, variables
	# variables are objects which you use to store a particular value in your program | you'll see how useful variables are for complicated & repetitive values
	
Learners = 35
Mentors = 5
Total = Learners + Mentors

print(Total)		#print() is a built-in Python function you'll use a lot to display output

Total = Learners + Mentors + Observers
Observers = 3
print(Total)

# Exercise B: range + loop + print

print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")

for i in range(5):
	print("Hello World!")	#What do you think this will output?

for i in range(5):
	print(i)

for bananas in range(5):
	print(bananas)


# Exercise C: Learn how to import specific functionality, starting with random 
	# So far, we've been using core Python software functionality that is always available to use when you are using a Python interpreter - built-in 
	# However, Python has loads of add-on software - these are called packages | currently 128k packages available, made & contributed by people in the community
	# Think about writing your own Python software package!
	# Once you've chosen the packages you want to use and installed them, you will then have the ability to 'import' specific modules within these packages
	# trinket has already chosen & set-up certain modules > 13 modules being available in the ?Modules tab
	# Let's use the random module
	# You can see some of the most useful commands that you can access by using the random module | technical name is command
	# 2 specific commands in the random module, randint & choice

import random

random.randint(0, 10)	#includes both end points

colours = []
colours = ["...", "...", "..."]
random.choice(colours)


# Exercise D: Introduce turtle module | Let's PROGRAM SOME VIRTUAL TURTLES!!

import turtle 	

#Make Turtle
turtle.Turtle()

#Appearance
turtle.shape("arrow", "turtle", "circle", "square", "triangle", "classic")

#'Methods of TurtleScreen/Screen
screen = turtle.getscreen()

#Turtle state
turtle.showturtle()	
turtle.hideturtle() 


# Exercise E: Make shape with dependent on number of sides e.g. ^4 equal sides than angle of each corner = 360 degrees / 4


length_of_side = 100
no_of_sides = 3
angle = 360/no_of_sides
turtle.forward(length_of_side)
turtle.right(angle)
turtle.forward(length_of_side)
turtle.right(angle)
turtle.forward(length_of_side)
turtle.right(angle)

# Exercise F: Make this triangle using a loop instead of repeating instructions 
# ... for loops are traditionally used when you have a block of code which you want to repeat a fixed number of times.


length_of_side = 100
no_of_sides = 3
angle = 360/no_of_sides

for i in range(no_of_sides):
	turtle.forward(length_of_side)
	turtle.right(angle)



# Exercise G: Let's make one firework

size_of_circle = 100
no_of_circles = 3
angle = 360/no_of_circles

for i in range(no_of_circles):
	turtle.circle(size_of_circle)
	turtle.right(angle)
	

# Exercise H: make multiple fireworks manually in different grid locations


# Exercise I: make multiple fireworks using a loop to choose random grid locations + use penup/down


# Exercise J: make firework size vary


# Exercise K: change firework colour + then make colour vary


list_of_colours = ["red", "yellow", "green", "blue", "purple"]

for i in range(10):
    turtle.penup()
    turtle.goto(random.randint(-100,100),random.randint(-100,100))
    turtle.pendown()
    turtle.pencolor(random.choice(list_of_colours))
    
    size_of_circle = random.randint(5, 10)
    no_of_circles = random.randint(5, 10)
    angle = 360/no_of_circles
    
    for i in range(no_of_circles):
    	turtle.circle(size_of_circle)
    	turtle.right(angle)



# Exercise L: make pensize smaller + set background colour





### Let's get our program to make lots of fireworks


import turtle
import random

screen = turtle.getscreen()
screen.bgcolor("black")

t = turtle.Turtle()
t.pensize(0.1)
t.hideturtle()

list_of_colours = [
    "medium blue", "cornflowerblue", "blue", "blue2", 
    "mediumpurple1", "turquoise", "aquamarine", 
    "mistyrose", "light yellow"
    ]

random.seed(555)

for i in range(30):
    t.penup()
    t.goto(random.randint(-150,150), random.randint(-150,150))
    t.pendown()
    t.pencolor(random.choice(list_of_colours))
    
    size_of_circles = random.randint(3, 40)
    no_of_circles = random.randint(9, 36)
    
    for j in range(no_of_circles):
        t.circle(size_of_circles)
        t.right(360/no_of_circles)
