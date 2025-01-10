import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Ui:
    def __init__(self, quiz_brain:QuizBrain):
        self.root = tk.Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_lbl = tk.Label(text=f"Score: 0/0", bg=THEME_COLOR)
        self.score_lbl.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=280, height=250, bg="white")
        self.q_text = self.canvas.create_text(150, 125, text="teste", width=250, font=("Arial", 15, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        true_img = tk.PhotoImage(file="images/true.png")
        false_img = tk.PhotoImage(file="images/false.png")
        self.true_button = tk.Button(image=true_img, highlightthickness=0, command=lambda:self._answer("True"), pady=20)
        self.true_button.grid(row=2, column=0)
        self.false_button = tk.Button(image=false_img, highlightthickness=0, command=lambda:self._answer("False"), pady=20)
        self.false_button.grid(row=2, column=1)
        self.quiz = quiz_brain
        self.next_question()
        self.root.mainloop()
        # self.question
        # self.answer
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text= q_text)
        else:
            self.canvas.itemconfig(self.q_text, text=f"You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def _answer(self, answer):
        if self.quiz.check_answer(answer) is True:
            self.canvas.config(bg="green")
            self.score_lbl.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        else:
            self.canvas.config(bg="red")
            self.score_lbl.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.root.after(1000, self.next_question)

