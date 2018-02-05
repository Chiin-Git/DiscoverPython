# WELCOME: to the Discover Python - Programming Virtual Turtles to draw Computer Graphics workshop
# This workshop is for people who've never done any coding before, or who've maybe done some programmimg in another language but never in Python

# So, to demo what you'll be programming in the next hour | computer-generated graphics

# Intro to me | Intro to mentors | Intro to you - who is in school/college/uni/working? So I'm hoping you're all new to Python?


# So let's just set the scene a bit and talk about Languages: first of all, let's talk about Natural Languages - English is my first language, but what's yours?
# So in the same way some of us communicate in a variety of Natural Languages to talk to different people, 
# ...people in Tech communicate in a variety of Computer Languages to talk to/work with different technologies 
# ...e.g. Computer Languages for writing instructions for robots, to make apps, 

# But today we're doing Python! So why Python? | Python is one of the most common & useful Computer Languages in Tech - the equivalent of English as a Natural Language
# ...so if you know Python, you have the power to do lots of cool things! Amongst the mentors in the room, we've done cool things in Python, like CyberSec, Robotics, Algos
# We'll show more examples of Python use-cases at the end if we have enough time

# BUT now let's start Discovering Python instead of talking about it!!

# 1. Set-up your personal programming environment - trinket | We're going to do x exercises, leading up to the Firework grahpic
# 1.x Make a new trinket, Save it, then Duplicate it and write new code


# Exercise A: Introduce console | Let's do some sums together | Shout your favourite number to me 

342 + 43298

# Exercise B: Variables | Writing a program/script - instead of single instructions, but what if we need the computer to follow a series of instructions? 
#...i.e. we want to write a program which has lots of steps to
#...then we want to create a Python script which the computer just runs all at once

#Calculate the number of people in this room, using named variables that the computer will store for this working session so you can re-use

Total = Learners + Mentors
Learners = 35
Mentors = 5
print(Total)

Total = Learners + Mentors + Observers
Observers = 3
print(Total)

# Exercise C: range + loop

range(5)

# Exercise C: Learn how to import packages, starting with random | #What are modules | Let's learn 2 specific commands in the random module, randint & choice

import random
random.randint(0, 10)
random.choice(colours)
colours = []
colours = ["...", "...", "..."]


# Exercise D: Introduce turtle module

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

turtle.pendown()
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



####Turtle Appearance


### Let's make one firework



### Let's make a few fireworks



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
