# Code written by - Amish Verma
# Original date of writing - 11/11/2021
# GitHub - www.github.com/thisisamish
# Twitter - www.twitter.com/thisisamish
# This project was created as a part of the #100DaysOfCode challenge I undertook
# as a part of "The Complete Python Pro Bootcamp for 2022" course by Angela Yu on Udemy.
# Please report any bugs you find; and if you want, then try make the code more efficient. Thank you!


import turtle
from turtle import Turtle, Screen
from random import choice, randint
from tkinter import *
from tkinter import messagebox

useless_variable = 0

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []
curr_turtle_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    color = choice(colors)
    colors.remove(color)
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


def diff_bw_lists(list1, list2):
    for item in list2:
        for element in list1:
            if item == element:
                list1.remove(item)
                return list1


curr_turtle_colors = diff_bw_lists(curr_turtle_colors, colors)


def let_user_bet():
    global useless_variable
    user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ").lower()
    if user_bet not in curr_turtle_colors:
        root = Tk()
        messagebox.showinfo(title="Error!", message="Please enter a valid color.")
        let_user_bet()
    else:
        useless_variable = 1
        return user_bet


user_bet_color = let_user_bet()

if useless_variable == 1:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if 220 - turtle.xcor() <= 10:
            turtle.forward(220 - turtle.xcor())
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet_color:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                print(f"You've lost! The {winning_color} is the winner.")
        else:
            random_distance = randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
