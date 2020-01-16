import tkinter as tk
from tkinter import *
import random
Win_Score=0
player_choice=""
random_choice=""

def randomchoice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

root= tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(background="light sky blue")

Label(root, text="Rock, Paper, Scissors game made by Nik Kronšek", bg="light sky blue", fg="black", font="Calibri 16 bold") .grid(row=1, column=0, sticky=S)

canvas=tk.Canvas(root, height=500, width=700, bg="light sky blue", bd=0, highlightthickness=0)
canvas.grid()

frame = tk.Frame(root, bg="DarkOliveGreen1", highlightbackground="black", highlightthickness=3)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

label1 = Label(frame, text=" ", bg="DarkOliveGreen1", font="Calibri 16 bold")
label1.grid(row=2, column=1)

def choice_to_number(choice):
    return {'Rock': 0, 'Paper': 1, 'Scissors': 2}[choice]


def number_to_choice(number):
    return {0: 'Rock', 1: 'Paper', 2: 'Scissors'}[number]

def label_win_change():
    label1.configure(text="Win!")
def label_lose_change():
    label1.configure(text="Lose!")
def label_draw_change():
    label1.configure(text="Draw!")

def results(player_choice, random_choice):
    random_choice_number=choice_to_number(random_choice)
    player_choice_number=choice_to_number(player_choice)
    if (player_choice_number==random_choice_number):
        label_draw_change()
    elif( (player_choice_number- random_choice_number) % 3== 1):
        label_win_change()
        global Win_Score
        Win_Score+=1
        label_score.config(text="Score: "+ str(Win_Score))
    else:
        label_lose_change()

def rock():
    global player_choice
    global random_choice
    player_choice="Rock"
    random_choice=randomchoice()
    label_random_choice.config(text="Computer choice: " + str(random_choice))
    label_player_choice.config(text="Player choice: Rock")
    results(player_choice, random_choice)
def paper():
    global player_choice
    global random_choice
    player_choice="Paper"
    random_choice=randomchoice()
    label_random_choice.config(text="Computer choice: " + str(random_choice))
    label_player_choice.config(text="Player choice: Paper")
    results(player_choice, random_choice)
def scissors():
    global player_choice
    global random_choice
    player_choice="Scissors"
    random_choice=randomchoice()
    label_random_choice.config(text="Computer choice: " + str(random_choice))
    label_player_choice.config(text="Player choice: Scissors")
    results(player_choice, random_choice)





label_random_choice=Label(frame, text="Computer choice: ", bg="DarkOliveGreen1", font="Calibri 12 italic")
label_random_choice.grid(row=2, column=2)
label_player_choice=Label(frame, text="Player choice: ", bg="DarkOliveGreen1", font="Calibri 12 italic")
label_player_choice.grid(row=2, column=0)



label_score=Label(frame, text="Score: ", bg="DarkOliveGreen1", font="Calibri 16 bold")
label_score.grid(row=1, column=1)


root.resizable(0,0)

button1=Button(frame, text="Rock", bg="gray40", bd=3, fg = "black", relief = RIDGE, height=6, width=25, command=lambda: rock())
button1.grid(row=0, column=0)
button2=Button(frame, text="Paper", bg="bisque", bd=3, fg = "black", relief = RIDGE, height=6, width=25, command=lambda: paper())
button2.grid(row=0, column=1)
button3=Button(frame, text="Scissors", bg="dark orchid", bd=3, fg = "black", relief = RIDGE, height=6, width=24, command=lambda: scissors())
button3.grid(row=0, column=2)

root.mainloop()
