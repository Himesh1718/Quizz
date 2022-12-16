from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(self.window, width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=250, font=('Arial', 20, 'italic'), text="Some question text", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(self.window, image=right_image, command=self.true_pressed, highlightthickness=0)
        self.right_button.grid(row=2, column=0)
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(self.window, image=wrong_image, command=self.false_pressed, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text="Score: {}".format(self.quiz.score))
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have finished the quiz!")
            self.right_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
