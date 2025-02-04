import tkinter as tk
from gui import GameGUI

def main():
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
