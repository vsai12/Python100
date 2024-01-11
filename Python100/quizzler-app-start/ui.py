from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
MY_FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, qb: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.qb = qb

        self.score_text = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.question_canvas.create_text(150,
                                                              125,
                                                              width=280,
                                                              text="Placeholder",
                                                              font=MY_FONT)
        self.next_question()

        self.checkmark_img = PhotoImage(file="images/true.png")
        self.checkmark_button = Button(image=self.checkmark_img, highlightthickness=0, command=self.true_pressed)
        self.checkmark_button.grid(row=2, column=0)

        self.cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=self.cross_img, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(row=2, column=1)
        self.window.mainloop()

    def next_question(self):
        self.question_canvas.config(bg="white")
        if self.qb.still_has_questions():
            self.score_text.config(text=f"Score: {self.qb.score}")
            q_text = self.qb.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.checkmark_button.config(state="disabled")
            self.cross_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.qb.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.qb.check_answer("False"))

    def give_feedback(self, ans: bool):
        if ans:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.next_question)

