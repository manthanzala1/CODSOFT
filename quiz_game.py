import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)
        
        self.answer_choices = []
        for i in range(4):
            choice = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            choice.pack(pady=5)
            self.answer_choices.append(choice)
        
        self.score = 0
        self.current_question = 0
        self.load_questions()
        self.display_question()

    def load_questions(self):
        # Load your quiz questions and answers here.
        # Store them in a list or dictionary.
        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["London", "Berlin", "Madrid", "Paris"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "choices": ["Earth", "Mars", "Jupiter", "Venus"],
                "correct_answer": "Mars"
            },
            {
                "question": "How many continents are there on Earth?",
                "choices": ["5", "6", "7", "8"],
                "correct_answer": "7"
            }
        ]

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.answer_choices[i].config(text=question_data["choices"][i])
        else:
            self.show_results()

    def check_answer(self, choice):
        question_data = self.questions[self.current_question]
        if self.answer_choices[choice]["text"] == question_data["correct_answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            correct_answer = question_data["correct_answer"]
            messagebox.showerror("Incorrect", f"Your answer is incorrect. The correct answer is {correct_answer}")
        
        self.current_question += 1
        self.display_question()

    def show_results(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
