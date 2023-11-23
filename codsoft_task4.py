import random
from tkinter import *

# DICTIONARY & VARIABLES
schema = {
    "ROCK": {"ROCK": 1, "PAPER": 0, "SCISSORS": 2},
    "PAPER": {"ROCK": 2, "PAPER": 1, "SCISSORS": 0},
    "SCISSORS": {"ROCK": 0, "PAPER": 2, "SCISSORS": 1}
}

comp_score = 0
player_score = 0
rounds_played = 0
max_rounds = 3

round_results = []

# FUNCTIONS
def outcome_handler(user_choice):
    global comp_score, player_score, rounds_played

    if rounds_played < max_rounds:
        outcomes = ["ROCK", "PAPER", "SCISSORS"]
        random_number = random.randint(0, 2)
        computer_choice = outcomes[random_number]
        result = schema[user_choice][computer_choice]

        player_choice_label.config(fg="red", text="PLAYER CHOICE: " + user_choice)
        computer_choice_label.config(fg="green", text="COMPUTER CHOICE: " + computer_choice)

        if result == 2:
            player_score += 2
            outcome_label.config(fg="blue", text="OUTCOME: PLAYER WINS")
        elif result == 1:
            player_score += 1
            comp_score += 1
            outcome_label.config(fg="blue", text="OUTCOME: DRAW")
        elif result == 0:
            comp_score += 2
            outcome_label.config(fg="blue", text="OUTCOME: COMPUTER WINS")

        player_score_label.config(text="PLAYER: " + str(player_score))
        computer_score_label.config(text="COMPUTER: " + str(comp_score))

        rounds_played += 1

        round_results.append((user_choice, computer_choice, player_score, comp_score))

        if rounds_played == max_rounds:
            if player_score > comp_score:
                outcome_label.config(fg="blue", text="GAME OVER: PLAYER WINS")
            elif player_score < comp_score:
                outcome_label.config(fg="blue", text="GAME OVER: COMPUTER WINS")
            else:
                outcome_label.config(fg="blue", text="GAME OVER: DRAW")

# New game function
def start_new_game():
    global comp_score, player_score, rounds_played, round_results
    comp_score = 0
    player_score = 0
    rounds_played = 0
    round_results = []
    player_score_label.config(text="PLAYER: 0")
    computer_score_label.config(text="COMPUTER: 0")
    player_choice_label.config(text="")
    computer_choice_label.config(text="")
    outcome_label.config(text="")
    results_text.config(text="")

# Display round results
def display_results():
    results_text.config(text="Round Results:\n")
    for i, result in enumerate(round_results):
        results_text.config(text=results_text.cget("text") + f"Round {i + 1}: Player - {result[2]}, Computer - {result[3]}\n")

# MAIN SCREEN
master = Tk()
master.geometry("600x400")
master.title("RPS")

# Labels
Label(master, text="ROCK PAPER SCISSORS", font=("calibri", 14)).grid(row=0, pady=10, padx=200, columnspan=3)

Label(master, text="PLEASE SELECT AN OPTION", font=("calibri", 12)).grid(row=1, pady=5, columnspan=3)

player_score_label = Label(master, text="PLAYER: 0", font=("calibri", 12))
player_score_label.grid(row=2, column=0, sticky="e")

computer_score_label = Label(master, text="COMPUTER: 0", font=("calibri", 12))
computer_score_label.grid(row=2, column=2, sticky="w")

player_choice_label = Label(master, font=("calibri", 12))
player_choice_label.grid(row=3, column=0, sticky="e")

computer_choice_label = Label(master, font=("calibri", 12))
computer_choice_label.grid(row=3, column=2, sticky="w")

outcome_label = Label(master, font=("calibri", 12))
outcome_label.grid(row=3, column=1)

# Buttons
Button(master, text="ROCK", width=15, command=lambda: outcome_handler("ROCK")).grid(row=4, column=0, padx=5, pady=5)
Button(master, text="PAPER", width=15, command=lambda: outcome_handler("PAPER")).grid(row=4, column=1, pady=5)
Button(master, text="SCISSORS", width=15, command=lambda: outcome_handler("SCISSORS")).grid(row=4, column=2, padx=5, pady=5)

# Replay button
replay_button = Button(master, text="REPLAY", width=15, command=start_new_game)
replay_button.grid(row=5, column=0, pady=10)

# Show results button
show_results_button = Button(master, text="SHOW RESULTS", width=15, command=display_results)
show_results_button.grid(row=5, column=2, pady=10)

# Display results section
results_text = Label(master, text="", font=("calibri", 12))
results_text.grid(row=6, column=0, columnspan=3)

master.mainloop()
