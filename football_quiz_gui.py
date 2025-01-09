import tkinter as tk
from tkinter import messagebox
import random

# Initialize variables
score = 0
tries = 3
question_index = 0

# List of questions and answers
questions = [
    ("Who is the team that won the 2023 African Champions League?", "alahly"),
    ("Who is the club with the most championships in Africa?", "alahly"),
    ("Who is the top scorer in the 2022 World Cup?", "mbappe"),
    ("Who won the Best Young Player award in the 2024 European Nations Cup?", "lamin yamal"),
    ("How many matches did the 2022 World Cup champion play during his participation (7, 8, 9, 6)?", "7"),
    ("Who is the national team that has won the most African Cup of Nations?", "egypt"),
    ("Which team won the 2010 FIFA World Cup?", "spain"),
    ("Which country has won the most FIFA World Cups?", "brazil"),
    ("Who scored the fastest goal in World Cup history?", "hakan sukur"),
    ("Who is the all-time top scorer in the Champions League?", "ronaldo"),
    ("Who won the 2020 UEFA Euro Championship?", "italy"),
    ("Which player has the most assists in a single EPL season?", "de bruyne"),
    ("Which African player won the Ballon d'Or in 1995?", "george weah"),
    ("Which club has won the most Champions League titles?", "real madrid"),
    ("Who won the Golden Boot in the 2014 FIFA World Cup?", "james rodriguez"),
    ("Who is the manager with the most EPL titles?", "ferguson"),
    ("Who is the youngest player to debut in La Liga?", "lamin yamal"),
    ("Which team has won the most Bundesliga titles?", "bayern munich"),
    ("Which country hosted the 2002 FIFA World Cup?", "japan and south korea"),
    ("Who scored a hat-trick in the 1966 World Cup final?", "geoff hurst"),
    ("Which club did Messi join in 2021 after leaving Barcelona?", "psg"),
    ("Which country won the first FIFA World Cup in 1930?", "uruguay"),
    ("Who is the all-time top scorer for the Egyptian national team?", "hossam hassan"),
    ("Which player won the Golden Ball at the 2018 World Cup?", "modric"),
    ("Who is the most expensive footballer in transfer history?", "neymar"),
    ("Which team won the treble in 1999?", "manchester united"),
    ("Which player is known as 'El Fenómeno'?", "ronaldo"),
    ("Which goalkeeper has the most clean sheets in EPL history?", "cech"),
    ("Who won the Copa America in 2021?", "argentina"),
    ("Who scored the 'Hand of God' goal?", "maradona"),
    ("Which team won the 2023 Women's World Cup?", "spain"),
    ("Who holds the record for most goals in a single calendar year?", "messi"),
    ("Which country has won the most Copa America titles?", "uruguay"),
    ("Who won the Golden Glove in the 2022 World Cup?", "emi martinez"),
]

# Shuffle questions for randomness
random.shuffle(questions)

# Function to handle answer submission
def submit_answer():
    global score, tries, question_index

    answer = answer_entry.get().strip().lower()
    if answer == questions[question_index][1]:
        score += 1
        messagebox.showinfo("Correct!", "🎉 Correct answer!")
    else:
        tries -= 1
        messagebox.showerror("Wrong!", f"❌ Wrong answer! The correct answer is: {questions[question_index][1]}")
    
    if tries == 0:
        messagebox.showerror("Game Over", "😢 You've run out of tries. Game over!")
        root.destroy()
        return

    question_index += 1
    if question_index < len(questions):
        question_label.config(text=questions[question_index][0])
        answer_entry.delete(0, tk.END)
        update_status()
    else:
        messagebox.showinfo("Congratulations!", f"🎉 You've completed the quiz! Final Score: {score}")
        root.destroy()

# Function to update the status
def update_status():
    status_label.config(text=f"Score: {score} | Tries Left: {tries}")

# Create GUI window
root = tk.Tk()
root.title("Football Quiz")
root.geometry("600x400")
root.configure(bg="#282c34")

# Header label
header_label = tk.Label(root, text="⚽ Football Quiz ⚽", font=("Arial", 20, "bold"), bg="#61afef", fg="white")
header_label.pack(pady=10, fill="x")

# Question label
question_label = tk.Label(root, text=questions[question_index][0], font=("Arial", 14), wraplength=500, bg="#282c34", fg="#98c379")
question_label.pack(pady=20)

# Answer entry
answer_entry = tk.Entry(root, font=("Arial", 14), bg="#e06c75", fg="white")
answer_entry.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), bg="#61afef", fg="white", command=submit_answer)
submit_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text=f"Score: {score} | Tries Left: {tries}", font=("Arial", 12), bg="#282c34", fg="#c678dd")
status_label.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Good Luck! 🏆", font=("Arial", 10), bg="#282c34", fg="#abb2bf")
footer_label.pack(side="bottom", pady=10)

# Run the GUI
root.mainloop()
