import tkinter as tk
import random

class ScrabbleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mthuli Buthelezi")
        self.root.geometry("400x300")
        self.root.configure(bg="#CD7F32")  # Using a hexadecimal color code for bronze

        self.words = ["umuntu", "itshitshi", "isiqoqelalwazi", "isithombe", "idlozi", "umphefumulo", "isihlalo",
                      "ulwandle", "imbiza", "ibhodwe", "imali", "intombi", "ubuthongo", "amathongo",
                      "lalela", "bhukuda", "idolobha", "ubudlelwano", "vuna", "vuba", "amasi",
                      "incwadi", "funda", "dlondlobala", "bala", "doba", "funza", "feba",
                      "vula", "inkohlakalo", "bhema", "phuza", "ukuba", "futhi", "phindaphinda",
                      "hambahamba", "dudula", "deda", "ubafo", "inkohliso", "ncoma", "gcoba"]
        self.used_words = set()
        self.points = 0
        self.total_rounds = 4
        self.current_round = 0
        self.timer = 60

        self.label = tk.Label(root, text="Unscramble the word:", bg="#CD7F32", font=("Arial", 14))
        self.label.pack(pady=10)

        self.word_label = tk.Label(root, text="", bg="#CD7F32", font=("Arial", 18, "bold"))
        self.word_label.pack()

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check_word)  # Binding Enter key to check_word method

        self.score_label = tk.Label(root, text="amaphuzu: 0", bg="#CD7F32", font=("Arial", 12))
        self.score_label.pack()

        self.timer_label = tk.Label(root, text="isikhathi esisele: 60", bg="#CD7F32", font=("Arial", 12))
        self.timer_label.pack()

        self.next_button = tk.Button(root, text="Qhubeka", command=self.next_word)
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)  # Initially disabled

        self.start_game()

    def start_game(self):
        self.next_button.config(state=tk.NORMAL)  # Enable the Next button to start the game
        self.timer_label.config(text="Time left: 60")
        self.timer = 60
        self.countdown()  # Start the countdown timer
        self.next_word()

    def next_word(self):
        self.entry.delete(0, tk.END)
        if self.current_round < self.total_rounds:
            word = random.choice(self.words)
            while word in self.used_words:
                word = random.choice(self.words)
            self.used_words.add(word)
            self.current_word = word
            scrambled_word = '|'.join(random.sample(word, len(word)))
            self.word_label.config(text=scrambled_word)
            self.current_round += 1
        else:
            self.show_final_score()

    def check_word(self, event=None):
        user_word = self.entry.get().upper()
        if user_word == self.current_word:
            self.points += 1
        self.score_label.config(text=f"Score: {self.points}/{self.current_round}")
        self.next_word()

    def countdown(self):
        if self.timer > 0:
            self.timer -= 1
            self.timer_label.config(text=f"Time left: {self.timer}")
            self.root.after(1000, self.countdown)
        else:
            self.show_final_score()

    def show_final_score(self):
        self.word_label.config(text="Game Over!")
        self.entry.pack_forget()
        self.next_button.pack_forget()
        self.score_label.config(text=f"Final Score: {self.points}/{self.total_rounds}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ScrabbleGame(root)
    root.mainloop()
