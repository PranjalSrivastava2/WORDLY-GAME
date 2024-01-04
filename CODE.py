import random

# List of words for the game
word_list = [
    'Apple', 'Mango', 'Lemon', 'Grape', 'Peach', 'Plum', 'Kiwi', 'Melon', 'Cherry', 'Water',
    'Beach', 'Brave', 'Climb', 'Dress', 'Eight', 'Fight', 'Grass', 'Hotel', 'Jumbo', 'Knife',
    'Latch', 'Magic', 'Nagin', 'North', 'Oasis', 'Peach', 'Queen', 'Radio', 'Smile', 'Table', 'Unity',
    'Viper', 'Watch', 'Xylos', 'Yacht', 'Zebra', 'Amber', 'Blend', 'Crisp', 'Diver', 'Eagle',
    'Fable', 'Glide', 'Haven', 'Inky', 'Jolly', 'Kiosk', 'Latch', 'Mirth', 'Nudge', 'Ocean',
    'Prism', 'Quota', 'Rapid', 'Snake', 'Tramp', 'Usher', 'Vigor', 'Whirl', 'Xenon', 'Yacht',
]

# Select a random word for the player to guess
target_word = random.choice(word_list).lower()
attempts = 6

# Initialize an empty list to store the guessed letters
guessed_letters = ['_'] * len(target_word)

print("Welcome to Wordle! You have 6 attempts to guess a word.")

while attempts > 0:
    print(" ".join(guessed_letters))
    guess = input(f"Enter your {len(target_word)}-letter guess: ").lower()
    
    if guess=='backendshow':
        print(target_word)

    if guess=='backendprint':
        print(word_list)
        
    if len(guess) != len(target_word):
        print(f"Please enter a {len(target_word)}-letter word.")
        continue

    correct_positions = 0
    correct_letters = 0

    for i in range(len(target_word)):
        if guess[i] == target_word[i]:
            correct_positions += 1
            guessed_letters[i] = guess[i]
        elif guess[i] in target_word:
            correct_letters += 1

    if correct_positions == len(target_word):
        print(f"Congratulations! You've guessed the word: {target_word}")
        break

    print(f"Correct letters in the right position: {correct_positions}")
    print(f"Correct letters in the wrong position: {correct_letters}")
    print(f"Attempts left: {attempts - 1}\n")

    attempts -= 1

if attempts == 0:
    print(f"Out of attempts. The word was: {target_word}")

print("Thank you for playing Wordle!")
