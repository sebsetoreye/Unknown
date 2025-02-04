import tkinter as tk
from game_logic import check_solution, generate_target
from threadding import start_timer



class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Target Game")

        # Generate a random target and available numbers
        self.target, self.available_numbers = generate_target()

        self.time_left = 30  # Time in seconds

        # Create and pack the widgets
        self.target_label = tk.Label(master, text=f"Target: {self.target}", font=('Arial', 20))
        self.target_label.pack()

        self.numbers_label = tk.Label(master, text=f"Available Numbers: {self.available_numbers}", font=('Arial', 16))
        self.numbers_label.pack()

        self.timer_label = tk.Label(master, text=f"Time Left: {self.time_left}s", font=('Arial', 16))
        self.timer_label.pack()

        self.user_input = tk.Entry(master, font=('Arial', 16))
        self.user_input.pack()

        self.check_button = tk.Button(master, text="Check Answer", command=self.check_input)
        self.check_button.pack()

        self.result_label = tk.Label(master, text="", font=('Arial', 16))
        self.result_label.pack()

        self.start_game()  # Start the timer when the game starts

    def check_input(self):
        answer = self.user_input.get()
        if check_solution(answer, self.target):
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text="Try again!", fg="red")

    def update_timer(self):
        """Update the timer every second."""
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
        else:
            self.timer_label.config(text="Time's up!")
            self.check_input()  # Handle what happens when time is up (e.g., check answer automatically)

    def start_game(self):
        """Start the timer for the game."""
        start_timer(self.update_timer, 1)  # Update the timer every second

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()
