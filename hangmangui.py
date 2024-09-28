import tkinter as tk
from tkinter import messagebox
import random


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x500")

        self.difficulty = None
        self.category = None
        self.word = ""
        self.guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

        self.create_start_menu()

    def create_start_menu(self):
        self.clear_widgets()

        tk.Label(self.root, text="Choose Difficulty", font=("Helvetica", 20)).pack(pady=20)

        difficulty_frame = tk.Frame(self.root)
        difficulty_frame.pack(pady=10)
        tk.Button(difficulty_frame, text="Easy", command=lambda: self.set_difficulty('easy')).pack(side=tk.LEFT,
                                                                                                   padx=10)
        tk.Button(difficulty_frame, text="Medium", command=lambda: self.set_difficulty('medium')).pack(side=tk.LEFT,
                                                                                                       padx=10)
        tk.Button(difficulty_frame, text="Hard", command=lambda: self.set_difficulty('hard')).pack(side=tk.LEFT,
                                                                                                   padx=10)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.create_category_menu()

    def create_category_menu(self):
        self.clear_widgets()

        tk.Label(self.root, text="Choose Category", font=("Helvetica", 20)).pack(pady=20)

        categories = ['Animals', 'Programming', 'Bird', 'Fruits', 'Countries', 'Vegetables', 'Computer Components']
        for category in categories:
            tk.Button(self.root, text=category, command=lambda c=category: self.start_game(c)).pack(pady=10)

    def start_game(self, category):
        self.category = category
        self.word = self.get_random_word(self.difficulty, self.category)
        self.guesses = []
        self.attempts_left = self.max_attempts
        self.create_game_widgets()

    def get_random_word(self, difficulty, category):
        words = {
            'Animals': {
                'easy': ["cat", "dog", "fish", "horse", "rabbit", "sheep", "lion", "tiger"],
                'medium': ["elephant", "giraffe", "rhinoceros", "bear", "kangaroo", "pig", "cheetah", "wolf"],
                'hard': ["hippopotamus", "pterodactyl", "chameleon", "zebra", "gorilla", "polarbear", "crocodile", "jaguar"]
            },
            'Programming': {
                'easy': ["loop", "array", "file", 'array', 'list', 'dataframe', 'string', 'character'],
                'medium': ["dictionary", "exception", "module", 'error', 'conditional', 'function'],
                'hard': ["asynchronous", "polymorphism", "encapsulation", 'semantic', 'syntex', 'valueerror']
            },
            'Bird': {
                'easy': ['hen', 'crow', 'parrot','peacock', 'sparrow', 'pigion', "owl"],
                'medium': ["eagle", "penguin", "falcon"],
                'hard': ["goshawk", "kingrail", "tern", "warbler"]
            },
            'Fruits': {
                'easy': ["apple", "pear", "grape", "banana", "cherry", 'mango' ],
                'medium': ["date", "kivi", "avogardo", "blueberry", "coriander", 'pineapple', 'watermelon', 'lichi'],
                'hard': ['jabuticaba', 'durian', 'miraclefruit', 'jatoba', 'acaiberry']
            },
            'Countries': {
                'easy': ['india', 'pakistan', 'england', 'japan', 'austrelia', 'france', 'italy'],
                'medium': ['germany', 'rome', 'afganistan', 'portugal', 'argentina', 'brazil'],
                'hard': ['nepal', 'myanmar', 'bhutan', 'bangladesh', 'egypt']
            },
            'Vegetables': {
                'easy': ['cauliflower', 'cabbage', 'carrot', 'radish', 'potato', 'tomato', 'onion'],
                'medium': ['ginger', 'garlic', 'pumpkin', 'capsicum'],
                'hard': ['turmeric', 'beetroot', 'coriander', 'broccoli']
            },
            'Computer Components': {
                'easy': ['monitor', 'printer', 'motherboard', 'drive', 'harddisk', 'desktop', 'keyboard', 'mouse'],
                'medium': ['ram', 'rom', 'cache', 'input', 'output', 'screen', 'cpu'],
                'hard': ['coolingfan', 'scanner', 'videocard', 'processor', 'graphics']
            },

        }
        return random.choice(words[category][difficulty])

    def create_game_widgets(self):
        self.clear_widgets()

        self.label_word = tk.Label(self.root, text=self.get_display_word(), font=("Helvetica", 24))
        self.label_word.pack(pady=20)

        self.entry_guess = tk.Entry(self.root, font=("Helvetica", 18))
        self.entry_guess.pack(pady=10)

        self.button_guess = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.button_guess.pack(pady=10)

        self.label_attempts = tk.Label(self.root, text=f"Attempts Left: {self.attempts_left}", font=("Helvetica", 18))
        self.label_attempts.pack(pady=20)

        self.label_status = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.label_status.pack(pady=20)

    def get_display_word(self):
        display_word = ' '.join([char if char in self.guesses else '_' for char in self.word])
        return display_word

    def make_guess(self):
        guess = self.entry_guess.get().strip().lower()
        self.entry_guess.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Guess", "Please enter a single letter.")
            return

        if guess in self.guesses:
            messagebox.showinfo("Info", "You already guessed that letter.")
            return

        self.guesses.append(guess)

        if guess in self.word:
            if all(char in self.guesses for char in self.word):
                self.label_status.config(text="Congratulations! You won!")
                self.button_guess.config(state=tk.DISABLED)
        else:
            self.attempts_left -= 1
            if self.attempts_left <= 0:
                self.label_status.config(text=f"Game Over! The word was '{self.word}'.")
                self.button_guess.config(state=tk.DISABLED)

        self.label_word.config(text=self.get_display_word())
        self.label_attempts.config(text=f"Attempts Left: {self.attempts_left}")

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
