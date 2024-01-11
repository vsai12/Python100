from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
row = data_dict[0]


def flip_card():
    card_canvas.itemconfig(canvas_img, image=card_back)
    word = row["English"]
    card_canvas.itemconfig(trans, text=word, fill="white")
    card_canvas.itemconfig(lang, text="English", fill="white")


def generate_word():
    global row, timer
    window.after_cancel(timer)
    row = random.choice(data_dict)
    card_canvas.itemconfig(canvas_img, image=card_fr)
    word = row["French"]
    card_canvas.itemconfig(trans, text=word, fill="black")
    card_canvas.itemconfig(lang, text="French", fill="black")

    timer = window.after(3000, flip_card)


def checkmark():
    global data_dict, row
    data_dict.remove(row)
    df = pd.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_fr = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_img = card_canvas.create_image(400, 263, image=card_fr)
lang = card_canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
trans = card_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
generate_word()
card_canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=checkmark)
correct_button.grid(row=1, column=1)

window.mainloop()
