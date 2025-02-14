from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ('Arial', 16, 'italic')

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # display
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, background=THEME_COLOR)


        # Label
        self.score_label = Label(text=f"Score: 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Questions appear here..",
            fill=THEME_COLOR,
            font=FONT,
            width=280 # to wrap the sentences.
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Button
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.true_pressed)
        self.true_button.config(highlightthickness=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.false_pressed)
        self.false_button.config(highlightthickness=0, bg=THEME_COLOR)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()



    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(tagOrId=self.question_text, text=q_text, fill=THEME_COLOR)
        else:
            self.canvas.itemconfigure(
                tagOrId=self.question_text, fill=THEME_COLOR,
                text=f"You've completed the quiz \nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.canvas.itemconfigure(tagOrId=self.question_text, fill='white')
        self.window.after(1000, self.get_next_question)
