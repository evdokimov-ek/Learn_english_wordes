from tkinter import *
from tkinter import PhotoImage
import pandas as pd
from random import randint


BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    columns = ['English', 'Russian']
    df = pd.read_csv('data/first1000.csv', names=columns)
word_number = randint(0, len(df)-1)


def new_word():
    global word_number, flip_timer
    window.after_cancel(flip_timer)
    word_number = randint(0, len(df)-1)
    english_word = df.iloc[word_number][0]
    canvas.itemconfig(word, text=english_word, fill="black")
    canvas.itemconfig(title, text="English", fill="black")
    canvas.itemconfig(cards_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title, text="Русский", fill="white")
    russian_word = df.iloc[word_number][1]
    canvas.itemconfig(word, text=russian_word, fill="white")
    canvas.itemconfig(cards_background, image=card_back_img)

def is_known():
    global df
    df = df.drop([word_number])
    df.to_csv('data/words_to_learn.csv', index=False)
    print(len(df))
    new_word()


window = Tk()
window.title("Learning English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
cards_background = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fil="black")
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fil="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=new_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

new_word()

window.mainloop()
