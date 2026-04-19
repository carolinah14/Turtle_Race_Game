from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle would win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


y = 130
for color in colors:
    race_turtle = Turtle(shape="turtle")
    race_turtle.color(color)
    race_turtle.penup()
    y = y - 30
    race_turtle.goto(x=-230, y= y)
    all_turtles.append(race_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_turtles:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won the race!")
            else:
                print(f"You've lost! The {winning_color} turtle won the race!")
            break

        random_distance = random.randint(0, 10)
        racer.forward(random_distance)







screen.exitonclick()

