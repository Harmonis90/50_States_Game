import turtle
import pandas


FONT = ("Monospace", 8, "normal")
screen = turtle.Screen()
screen.title("U.S. States Game!")
USA_image = "blank_states_img.gif"
screen.addshape(USA_image)
turtle.shape(USA_image)

states_df = pandas.read_csv("50_states.csv")
states = states_df.state.to_list()


correct_states = []



def guess_state(guess):
    player_guess = guess
    if player_guess == "Remaining":
        print(str(50 - len(correct_states)) + " states left.")
    elif player_guess in states and player_guess not in correct_states:
        correct_states.append(player_guess)
        new_turtle = turtle.Turtle()
        new_turtle.ht()
        new_turtle.penup()
        state_coords = states_df[states_df.state == player_guess]
        new_turtle.goto(int(state_coords.x), int(state_coords.y))
        new_turtle.write(f"{player_guess}", align="center", font=FONT)

    else:
        print("Try Again!")


while len(correct_states) < 50:
    get_guess = turtle.textinput(title="Guess The States", prompt="Name A State bitch!").title()
    lives = guess_state(get_guess)

screen.mainloop()