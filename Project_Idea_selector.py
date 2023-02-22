import tkinter as tk

#coding with sagar 

class ProjectIdeaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Project Ideas")

        self.language_label = tk.Label(self.master, text="Select a language:", font=("Helvetica", 14))
        self.language_label.pack(pady=10)

        self.language_var = tk.StringVar(self.master)
        self.language_var.set("Python")
        self.language_dropdown = tk.OptionMenu(self.master, self.language_var, "Python", "Java", "C++", "JavaScript")
        self.language_dropdown.pack(pady=10)

        self.idea_label = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.idea_label.pack(pady=10)

        self.generate_button = tk.Button(self.master, text="Generate Idea", command=self.generate_idea)
        self.generate_button.pack(pady=10)

    def generate_idea(self):
        language = self.language_var.get()
        if language == "Python":
            ideas = [
                "A weather app that shows the current weather conditions and forecast",
                "A to-do list app with a task manager and reminders",
                "A web scraper that collects data from websites and stores it in a database",
                "A simple game like Tic Tac Toe or Snake",
                "A chatbot that can answer questions and have conversations",
            ]
        elif language == "Java":
            ideas = [
                "A simple e-commerce website with a shopping cart",
                "A music player app with a library of songs",
                "A notes app with the ability to add, edit, and delete notes",
                "A location-based app that shows nearby restaurants and cafes",
                "A stock market app that tracks stocks and provides real-time updates",
            ]
        elif language == "C++":
            ideas = [
                "A program that simulates the spread of a virus in a population",
                "A program that generates fractal patterns",
                "A program that implements a search algorithm like binary search or linear search",
                "A program that generates mazes and solves them",
                "A program that implements a sorting algorithm like bubble sort or insertion sort",
            ]
        elif language == "JavaScript":
            ideas = [
                "A website that generates random quotes from famous people",
                "A weather app that shows the current weather conditions and forecast",
                "A to-do list app with a task manager and reminders",
                "A quiz app that tests your knowledge on a particular subject",
                "A calculator app that performs basic arithmetic operations",
            ]
        else:
            ideas = []
        import random
        idea = random.choice(ideas)
        self.idea_label.config(text="Project idea: {}".format(idea))

root = tk.Tk()
app = ProjectIdeaApp(root)
root.mainloop()
