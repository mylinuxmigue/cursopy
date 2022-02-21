from turtle import *
from pandas import *

screen = Screen()
screen.title('States Games')

image = 'blank_states_img.gif'
screen.addshape(image)
shape(image)

data = read_csv('50_states.csv')


answer_state = screen.textinput(title='Guess the state', prompt="What is another state's name?")
if answer_state in data['state']:
    print(answer_state)

screen.mainloop()