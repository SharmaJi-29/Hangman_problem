import random

def choose_random_category():
    categories = {
        'Fruits': ["apple", "banana", "cherry", "date", "elderberry", 'mango', 'kivi', 'lichi', 'blueberry', 'berry', 'pineapple', 'watermelon', 'maxmelon'],
        'Countries': ["australia", "brazil", "canada", "denmark", "egypt", 'india', 'pakistan', 'afganistan', 'bhutan', 'nepal', 'myanmar', 'swedan', 'korea', 'japan'],
        'Birds': ['eagle', 'hen', 'crow', 'parrot', 'penguin', 'falcon', 'peacock', 'sparrow', 'pigion'],
        'Animal' : ['dog', 'cat', 'cow', 'sheep', 'rabbit', 'horse', 'lion', 'bear', 'deer', 'cheetah', 'fox', 'pig', "elephant", "giraffe", "tiger", "kangaroo", "zebra"],
        'Vegetables' : ['cauliflower', 'broccoli', 'cabbage', 'coriander', 'carrot', 'radish', 'beetroot', 'potato', 'tomato', 'pumpkin', 'onion', 'ginger', 'capsicum'],
        'Computer Components' : ['cpu', 'mouse', 'keyboard', 'motherboard', 'ram', 'drive', 'disk', 'cache', 'printer', 'monitor', 'desktop'],
        'Companies' :  ['tata', 'reliance', 'hdfc', 'airtel', 'apple', 'miscrosoft', 'meta', 'nvidia', 'google', 'amazon', 'flipcart']
    }
    category = random.choice(list(categories.keys()))
    return category, categories[category]

def choose_random_difficulty():
    difficulties = {
        'easy': 10,
        'medium': 7,
        'hard': 5
    }

    difficulty = random.choice(list(difficulties.keys()))
    return difficulty, difficulties[difficulty]

def display_board(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    category, word_list = choose_random_category()
    word = random.choice(word_list)
    guessed_letters = set()
    
    difficulty, attempts = choose_random_difficulty()
    guessed_word = False

    print(f"Category: {category}")
    print(f"Difficulty: {difficulty.capitalize()}")
    print(display_board(word, guessed_letters))

    while attempts > 0 and not guessed_word:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Incorrect. You have {attempts} attempts left.")

        current_display = display_board(word, guessed_letters)
        print(current_display)

        if '_' not in current_display:
            guessed_word = True

    if guessed_word:
        print(f"Congratulations! You guessed the word '{word}' correctly!")
    else:
        print(f"Sorry, you're out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    hangman()