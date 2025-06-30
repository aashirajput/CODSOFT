import tkinter as tk
import random

# Create main window
app = tk.Tk()
app.title("Rock Paper Scissors")
app.geometry("350x400")
app.configure(bg="#F0F8FF")

# Initialize scores
player_points = 0
computer_points = 0

# Function to decide the winner
def check_winner(player, computer):
    global player_points, computer_points

    if player == computer:
        result_text.set(f"Both selected {player}. It's a Draw!")
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        player_points += 1
        result_text.set(f"You chose {player}, Computer chose {computer}. You Win!")
    else:
        computer_points += 1
        result_text.set(f"You chose {player}, Computer chose {computer}. Computer Wins!")

    score_text.set(f"Score: You {player_points} - {computer_points} Computer")

# Function to handle player choice
def player_choice(choice):
    computer_move = random.choice(["Rock", "Paper", "Scissors"])
    check_winner(choice, computer_move)

# Function to reset game
def reset_game():
    global player_points, computer_points
    player_points = 0
    computer_points = 0
    result_text.set("Start Playing!")
    score_text.set("Score: You 0 - 0 Computer")

# UI Elements
heading = tk.Label(app, text="Rock Paper Scissors Game", font=("Verdana", 16, "bold"), bg="#F0F8FF")
heading.pack(pady=15)

result_text = tk.StringVar()
result_text.set("Start Playing!")
result_label = tk.Label(app, textvariable=result_text, font=("Arial", 12), bg="#F0F8FF", wraplength=300)
result_label.pack(pady=10)

score_text = tk.StringVar()
score_text.set("Score: You 0 - 0 Computer")
score_label = tk.Label(app, textvariable=score_text, font=("Arial", 12), bg="#F0F8FF")
score_label.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(app, bg="#F0F8FF")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: player_choice("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: player_choice("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: player_choice("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Reset Button
reset_btn = tk.Button(app, text="Reset Game", command=reset_game, bg="#FF7F50", fg="white")
reset_btn.pack(pady=10)

# Start the app
app.mainloop()
