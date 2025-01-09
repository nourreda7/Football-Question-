import tkinter as tk
from tkinter import messagebox
import random

# Initialize variables
score = 0
tries = 3
question_index = 0

# List of questions and answers
questions = [
    ("Who is the team that won the 2023 African Champions League?", ["Al Ahly", "Wydad", "Zamalek", "Esperance"], "Al Ahly"),
    ("Who is the club with the most championships in Africa?", ["Al Ahly", "TP Mazembe", "Zamalek", "Raja"], "Al Ahly"),
    ("Who is the top scorer in the 2022 World Cup?", ["Messi", "Mbappe", "Ronaldo", "Neymar"], "Mbappe"),
    ("Who won the Best Young Player award in the 2024 European Nations Cup?", ["Jude Bellingham", "Lamine Yamal", "Pedri", "Musiala"], "Lamine Yamal"),
    ("How many matches did the 2022 World Cup champion play during his participation (7, 8, 9, 6)?", ["7", "8", "9", "6"], "7"),
    ("Who is the national team that has won the most African Cup of Nations?", ["Egypt", "Cameroon", "Nigeria", "Ivory Coast"], "Egypt"),
    ("Which team won the 2010 FIFA World Cup?", ["Spain", "Netherlands", "Germany", "Argentina"], "Spain"),
    ("Which country has won the most FIFA World Cups?", ["Brazil", "Germany", "Italy", "Argentina"], "Brazil"),
    ("Who scored the fastest goal in World Cup history?", ["Hakan Sukur", "Maradona", "Pele", "Zinedine Zidane"], "Hakan Sukur"),
    ("Who is the all-time top scorer in the Champions League?", ["Ronaldo", "Messi", "Lewandowski", "Benzema"], "Ronaldo"),
    ("Who won the 2020 UEFA Euro Championship?", ["Italy", "England", "France", "Portugal"], "Italy"),
    ("Which player has the most assists in a single EPL season?", ["De Bruyne", "Harry Kane", "David Silva", "Salah"], "De Bruyne"),
    ("Which African player won the Ballon d'Or in 1995?", ["George Weah", "Samuel Eto'o", "Didier Drogba", "Mohamed Salah"], "George Weah"),
    ("Which club has won the most Champions League titles?", ["Real Madrid", "Barcelona", "Bayern Munich", "AC Milan"], "Real Madrid"),
    ("Who won the Golden Boot in the 2014 FIFA World Cup?", ["James Rodriguez", "Lionel Messi", "Thomas Muller", "Robin van Persie"], "James Rodriguez"),
    ("Who is the manager with the most EPL titles?", ["Sir Alex Ferguson", "Pep Guardiola", "Jose Mourinho", "Arsène Wenger"], "Sir Alex Ferguson"),
    ("Who is the youngest player to debut in La Liga?", ["Lamine Yamal", "Ansu Fati", "Vinícius Júnior", "Rodrygo"], "Lamine Yamal"),
    ("Which team has won the most Bundesliga titles?", ["Bayern Munich", "Borussia Dortmund", "Hamburg", "Bayer Leverkusen"], "Bayern Munich"),
    ("Which country hosted the 2002 FIFA World Cup?", ["Japan and South Korea", "Germany", "South Africa", "Brazil"], "Japan and South Korea"),
    ("Who scored a hat-trick in the 1966 World Cup final?", ["Geoff Hurst", "Pele", "Eusebio", "Bobby Charlton"], "Geoff Hurst"),
    ("Which club did Messi join in 2021 after leaving Barcelona?", ["PSG", "Manchester City", "Juventus", "Inter Milan"], "PSG"),
    ("Which country won the first FIFA World Cup in 1930?", ["Uruguay", "Brazil", "Argentina", "Italy"], "Uruguay"),
    ("Who is the all-time top scorer for the Egyptian national team?", ["Hossam Hassan", "Mohamed Salah", "Ahmed Fathi", "Amr Zaki"], "Hossam Hassan"),
    ("Which player won the Golden Ball at the 2018 World Cup?", ["Luka Modric", "Kylian Mbappe", "Antoine Griezmann", "Cristiano Ronaldo"], "Luka Modric"),
    ("Who is the most expensive footballer in transfer history?", ["Neymar", "Kylian Mbappe", "Lionel Messi", "Cristiano Ronaldo"], "Neymar"),
    ("Which team won the treble in 1999?", ["Manchester United", "Barcelona", "Bayern Munich", "Chelsea"], "Manchester United"),
    ("Which player is known as 'El Fenómeno'?", ["Ronaldo", "Luis Suárez", "Gareth Bale", "Diego Maradona"], "Ronaldo"),
    ("Which goalkeeper has the most clean sheets in EPL history?", ["Petr Cech", "David De Gea", "Jens Lehmann", "Joe Hart"], "Petr Cech"),
    ("Who won the Copa America in 2021?", ["Argentina", "Brazil", "Chile", "Colombia"], "Argentina"),
    ("Who scored the 'Hand of God' goal?", ["Diego Maradona", "Pele", "Lionel Messi", "Ronaldo"], "Diego Maradona"),
    ("Which team won the 2023 Women's World Cup?", ["Spain", "USA", "Germany", "Japan"], "Spain"),
    ("Who holds the record for most goals in a single calendar year?", ["Lionel Messi", "Cristiano Ronaldo", "Robert Lewandowski", "Kylian Mbappe"], "Lionel Messi"),
    ("Which country has won the most Copa America titles?", ["Uruguay", "Brazil", "Argentina", "Chile"], "Uruguay"),
    ("Who won the Golden Glove in the 2022 World Cup?", ["Emi Martinez", "Thibaut Courtois", "Hugo Lloris", "Manuel Neuer"], "Emi Martinez"),
    ("Which club did Cristiano Ronaldo join in 2021?", ["Manchester United", "Real Madrid", "Juventus", "PSG"], "Manchester United"),
    ("Who scored the most goals in the 2022-2023 Premier League season?", ["Erling Haaland", "Harry Kane", "Mohamed Salah", "Bruno Fernandes"], "Erling Haaland"),
]

# Shuffle questions for randomness
random.shuffle(questions)

# Function to handle answer submission via buttons
def check_answer(selected_answer):
    global score, tries, question_index

    correct_answer = questions[question_index][2]
    if selected_answer == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "🎉 Correct answer!")
    else:
        tries -= 1
        messagebox.showerror("Wrong!", f"❌ Wrong answer! The correct answer is: {correct_answer}")

    # Update the status after answering
    update_status()

    if tries == 0:
        messagebox.showerror("Game Over", "😢 You've run out of tries. Game over!")
        root.destroy()
        return

    question_index += 1
    if question_index < len(questions):
        update_question()
    else:
        messagebox.showinfo("Congratulations!", f"🎉 You've completed the quiz! Final Score: {score}")
        root.destroy()

# Function to update the question and answer buttons
def update_question():
    global question_index
    question_label.config(text=questions[question_index][0])

    # Clear existing answer buttons
    for button in answer_buttons:
        button.destroy()

    # Create new answer buttons
    choices = questions[question_index][1]
    for choice in choices:
        button = tk.Button(root, text=choice, font=("Arial", 14), bg="#61afef", fg="white", 
                           command=lambda c=choice: check_answer(c))
        button.pack(pady=5)
        answer_buttons.append(button)

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

# List to store the answer buttons
answer_buttons = []

# Call the update_question function to set the first question
update_question()

# Status label
status_label = tk.Label(root, text=f"Score: {score} | Tries Left: {tries}", font=("Arial", 12), bg="#282c34", fg="#c678dd")
status_label.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Good Luck! 🏆", font=("Arial", 10), bg="#282c34", fg="#abb2bf")
footer_label.pack(side="bottom", pady=10)

# Run the GUI
root.mainloop()
