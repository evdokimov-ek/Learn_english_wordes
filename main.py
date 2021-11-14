from tkinter import *
from tkinter import PhotoImage
import pandas as pd
from random import randint


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- READ DATA ------------------------------- #
columns = ['English', 'Russian']
df = pd.read_csv('data/first1000.csv', names=columns)

def new_word():
    word_number = randint(0, len(df)-1)
    english_word = df.iloc[word_number][0]
    russian_word = df.iloc[word_number][1]
    canvas.itemconfig(word, text=english_word)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Learning English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fil="black")
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fil="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=new_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=new_word)
known_button.grid(row=1, column=1)



window.mainloop()
