import random

# - Will generate number between 1 to difficulty and save it to secret_number
def generate_number(difficulty):
    secret = random.randint(1, difficulty)
    return secret

# - Will prompt the user for a number between 1 to difficulty and return the number.
def get_guess_from_user(diffculty):
    return int(input(f"Enter a number between 1 and {diffculty}: "))

# - Will compare the secret generated number to the one prompted by the get_guess_from_user.
def compare_results(guess, secret):
    return guess == secret

# - Will call the functions above and play the game. Will return True / False if the user lost or won.
def play(difficulty):
    secret = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(guess, secret)


print(play(4))
