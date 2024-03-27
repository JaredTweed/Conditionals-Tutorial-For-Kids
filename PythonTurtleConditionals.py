# Create a turtle named "ourTurtle"
# All the text to the right of a hashtag "#" is 
# a “comment” that is ignored by the computer.
import turtle
screen = turtle.Screen()
ourTurtle = turtle.Turtle()
ourTurtle.shape("turtle")

# This code moves our turtle 100 pixels 
# to the right, and 100 pixels up.
ourTurtle.setx(100) # right 100 pixels
ourTurtle.sety(100) # up 100 pixels

# # If the turtle's x-coordinate is greater than 50, 
# # change the turtle's and the screen's color to green.
if ourTurtle.xcor() > 50:
  ourTurtle.color("green")
  screen.bgcolor("lightgreen")
else:
  ourTurtle.color("purple")
  screen.bgcolor("lavender")

if False:
  ourTurtle.color("green")
  screen.bgcolor("lightgreen")
elif False:
  ourTurtle.color("purple")
  screen.bgcolor("lavender")
elif True:
  ourTurtle.color("blue")
  screen.bgcolor("lightblue")
elif True:
  ourTurtle.color("red")
  screen.bgcolor("pink")
elif False:
  ourTurtle.color("yellow")
  screen.bgcolor("lightyellow")
else:
  ourTurtle.color("orange")
  screen.bgcolor("peachpuff")

# codeAfterIfAndElseStatements = 'here'

# show <, >, <=, >=, ==, !=, not, and, or
# For later use: ourTurtle.xcor() > 20 and ourTurtle.ycor() > 20
  
# Keep the window open until it is closed by the user
turtle.done()
