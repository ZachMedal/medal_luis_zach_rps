# This file was created by: Zach Medal on 9/19/23

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
'''

# import package
import random
import turtle

# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h= 256, 204

scissors_w, scissors_h = 256, 170

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="black")

# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image and computer rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')

# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
comp_rock_instance = turtle.Turtle()

# add the rock image as a shape
screen.addshape(rock_image)

# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)

# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()

# assign vars for rock position
rock_pos_x = -300
rock_pos_y = 0

# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)

# setup the paper image and computer paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')

# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
comp_paper_instance = turtle.Turtle()

# add the paper image as a shape
screen.addshape(paper_image)

# attach the paper_image to the paper_instance
paper_instance.shape(paper_image)

# remove the pen option from the paper_instance so it doesn't draw lines when moved
paper_instance.penup()

# assign vars for paper position
paper_pos_x = 0
paper_pos_y = 0

# set the position of the paper_instance
paper_instance.setpos(paper_pos_x,paper_pos_y)

# setup the scissors image and computer using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')

# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
comp_scissors_instance = turtle.Turtle()

# add the scissors image as a shape
screen.addshape(scissors_image)

# attach the scissors_image to the scissors_instance
scissors_instance.shape(scissors_image)

# remove the pen option from the scissors_instance so it doesn't draw lines when moved
scissors_instance.penup()

# assign vars for scissors position

scissors_pos_x = 300
scissors_pos_y = 0

# set the position of the scissors_instance
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

# instantiate a generic turtle
text = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('purple')

# hide that turtle
text.hideturtle()

# instantiate a generic turtle
text.outcome = turtle.Turtle()
text.outcome.color('purple')

# hide that turtle
text.hideturtle()


# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and\
    y>obj.pos()[1] - h/2:
        return True
    else:
        return False
    
user_choice = "nothing"

# function that passes through wn onlick
def mouse_pos(x, y):
    if collide(x,y,rock_instance,rock_w,rock_h):
        text.clear()
        text.write("you chose rock!!!", False, "left", ("Arial", 24, "normal"))
        paper_instance.hideturtle()
        scissors_instance.hideturtle() 
        user_choice = "rock"
    elif collide(x,y,paper_instance,paper_w,paper_h):
        text.clear()
        text.write("you chose paper!!!", False, "left", ("Arial", 24, "normal"))
        rock_instance.hideturtle()
        scissors_instance.hideturtle()
        paper_instance.backward(300)
        user_choice = "paper"
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        text.clear()
        text.write("you chose scissors!!!", False, "left", ("Arial", 24, "normal"))
        rock_instance.hideturtle()
        paper_instance.hideturtle()
        scissors_instance.backward(550)
        user_choice = "scissors"
    else:
        return print("come on choose something")
    
# define computer choice
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)

    if computer_choice == "rock":
        comp_rock_instance.shape(rock_image)
        comp_rock_instance.penup()
        comp_rock_instance.setpos(300,0)
        if user_choice == "paper":
            text.outcome.write("You Win!!!", False, "Center", ("Arial", 24, "normal"))
        elif user_choice == "scissors":
            text.outcome.write("You Lose!!!", False, "Center", ("Arial", 24, "normal"))
        else:
            text.outcome.write("Tie!!!", False, "Center", ("Arial", 24, "normal"))
    elif computer_choice == "paper":
        comp_paper_instance.shape(paper_image)
        comp_paper_instance.penup()
        comp_paper_instance.setpos(300,0)
        if user_choice == "scissors":
            text.outcome.write("You Win!!!", False, "Center", ("Arial", 24, "normal"))
        elif user_choice == "rock":
            text.outcome.write("You Lose!!!", False, "Center", ("Arial", 24, "normal"))
        else:
            text.outcome.write("Tie!!!", False, "Center", ("Arial", 24, "normal"))
    else:
        computer_choice == "scissors"
        comp_scissors_instance.shape(scissors_image)
        comp_scissors_instance.penup()
        comp_scissors_instance.setpos(300,0)
        if user_choice == "rock":
            text.outcome.write("You Win!!!", False, "Center", ("Arial", 24, "normal"))
        elif user_choice == "paper":
            text.outcome.write("You Lose!!!", False, "Center", ("Arial", 24, "normal"))
        else:
         text.outcome.write("Tie!!!", False, "Center", ("Arial", 24, "normal"))




# Starting text of the game
text.penup()
text.setpos(-375,150)
text.write("Welcome! Choose the option rock, paper, or scissors", False, "left", \
           ("Arial", 24, "normal"))







# Keep canvas on 
screen.onclick(mouse_pos)

# runs mainloop for Turtle - required to be last
screen.mainloop()

