import random
import tkinter as tk

choices = ["rock", "paper", "scissors"]
wins_of_user, wins_of_computer, rounds_drawn = 0, 0, 0


def play_game(user_choice):
    global wins_of_user, wins_of_computer, rounds_drawn
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "This round was a draw!"
        rounds_drawn = rounds_drawn + 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win this round!"
        wins_of_user = wins_of_user + 1
    else:
        result = "Computer wins this round!"
        wins_of_computer = wins_of_computer + 1

    update_display(user_choice, computer_choice, result)


def update_display(user_choice, computer_choice, result):
    user_choice_label.config(text="Your choice: " + user_choice)
    computer_choice_label.config(text="Computer choice: " + computer_choice)
    user_wins_label.config(text="Number of user wins: " + str(wins_of_user))
    computer_wins_label.config(text="Number of computer wins: " + str(wins_of_computer))
    result_label.config(text=result)


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")

choice_label = tk.Label(root, text="Choose Rock, Paper, or Scissors!")
choice_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

user_choice_label = tk.Label(root, text="")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="")
computer_choice_label.pack()

user_wins_label = tk.Label(root, text="Number of user wins: " + str(wins_of_user))
user_wins_label.pack()

computer_wins_label = tk.Label(root, text="Number of computer wins: " + str(wins_of_computer))
computer_wins_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
