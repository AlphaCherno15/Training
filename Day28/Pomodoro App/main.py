from tkinter import *
import math as mt
# ---------------------------- CONSTANTS ------------------------------ #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ---------------------------- #
def reset_timer():
    global reps, timer
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text='25:00')
    timer_label.config(text="Start", fg=GREEN)
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------ #
def start_timer():
    global reps
    work_setting = 10 #WORK_MIN * 60
    short_break = 5 #SHORT_BREAK_MIN * 60
    long_break = 7 #LONG_BREAK_MIN * 60
    if reps == 7:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break)
        reps = 0
    elif reps % 2 == 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_setting)
        reps += 1
    elif reps % 2 != 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break)
        reps += 1
# ---------------------------- COUNTDOWN MECHANISM ---------------------#
def count_down(count):
    global timer
    # "01:00 timer format"
    count_minute = mt.floor(count / 60)
    count_seconds = count % 60
    if count_minute < 10:
        count_minute = f'0{count_minute}'
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'
    canvas.itemconfig(timer_text, text=f'{count_minute}:{count_seconds}')
    if count > 0:
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        session = mt.floor(reps/2)
        for _ in range(session):
            marks += "✔"
        check_mark.config(text=marks, fg=GREEN)
# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text='25:00', fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)
timer_label = Label(text="Start", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)
start_button = Button(text="Start", command=start_timer, font=(FONT_NAME, 10, "bold"), highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 10, "bold"), highlightthickness=0)
reset_button.grid(row=2, column=2)
# check_var = IntVar()
# check = Checkbutton(text="✔", variable=check_var, fg=GREEN, bg=YELLOW)
# check.grid(row=3, column=1)
check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)
root.mainloop()
