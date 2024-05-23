import turtle as t
import random
screen = t.Screen()
screen.setup(width=500, height=400)
color_list = ['red', 'green', 'blue', 'orange', 'yellow', 'brown']
user_bet = t.textinput("Make a bet", 'Bet on turtle color to win')
all_turtles = []
for i in range(6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(-230, -130 + i*50)
    all_turtles.append(new_turtle)
race_on = True
while race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() > 200:
            race_on = False
            if turtle.fillcolor() == user_bet:
                print("You won.")
            else:
                print("You loose.")
            print(f"{turtle.fillcolor()} turtle won the race.")


screen.exitonclick()
