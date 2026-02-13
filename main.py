import turtle
import pandas

image = "map.gif"
df_path = "administrative_divisions.csv"

screen = turtle.Screen()
screen.setup(621,720)
screen.title("Guess the Indian States Game")
screen.addshape(image)
turtle.shape(image)

def write(x,y,answer):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(x,y)
    text.write(answer,False,"center",("courier",8,"bold"))

data = pandas.read_csv(df_path)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

guessed_state = []

while len(guessed_state) < 36 :
    answer_state = turtle.textinput(f"Guess the State: {len(guessed_state)}/36", "What's another administrative division ?").title()

    if answer_state == "Exit":
        break

    if answer_state in data.state.to_list():
        guessed_state.append(answer_state)
        state = data[data["state"] == answer_state]
        x_cor = state.x.to_list()[0]
        y_cor = state.y.to_list()[0]
        write(x_cor,y_cor,answer_state)

missed_administrative_div = []
for state in data.state.to_list():
    if state not in guessed_state :
        missed_administrative_div.append(state)
missed_dict = {"Missed Administrative Divisions" : missed_administrative_div}
df = pandas.DataFrame(missed_dict)
df.to_csv("Missed_administrative_divisions.csv")


screen.exitonclick()