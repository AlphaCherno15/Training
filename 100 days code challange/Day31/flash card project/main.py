from tkinter import *
import pandas as pd, random as rd, time
# ---------------------------- Constants------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Ariel", 40, "italic")
FONT_2 = ("Ariel", 60, "bold")
try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
# ---------------------------- Commands ------------------------------- #
def get_wrong():
    global timer
    generate()
    root.after_cancel(timer)
    canvas.itemconfig(card, image=image_front)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    timer = root.after(3000, flip)
def get_right():
    data_dict.remove(data_dict[choice])
    data2 = pd.DataFrame(data_dict)
    data2.to_csv("data/word_to_learn.csv", index=False)
    get_wrong()

# ---------------------------- word generator ------------------------------- #
def generate():
    global french_word, english_word, choice
    choice = rd.randint(1, len(data_dict) - 1)
    french_word = data_dict[choice]["French"]
    english_word = data_dict[choice]["English"]
generate()
# ---------------------------- flip ------------------------------- #
def flip():
    canvas.itemconfig(card, image=image_back)
    canvas.itemconfig(language_text, fill="white")
    canvas.itemconfig(word_text, fill="white")
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=english_word)
    root.after_cancel(timer)
# ---------------------------- UI SETUP ------------------------------- #
# main window
root = Tk()
root.title("Flashy")
root.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
timer = root.after(3000, flip)
# image path
image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
# canvas setup
canvas = Canvas(width=850, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(430, 300, image=image_front)
canvas.grid(row=0, column=0, columnspan=2)
language_text = canvas.create_text(425, 150, text= "French", fill="black", font=FONT_1)
word_text = canvas.create_text(425, 300, text= french_word, fill="black", font=FONT_2)
# Buttons
wrong_button = Button(image=wrong_image, highlightthickness=0, command=get_wrong)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, command=get_right)
right_button.grid(row=1, column=1)

root.mainloop()