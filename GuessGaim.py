import random

# - Will generate number between 1 to difficulty and save it to secret_number
def generate_number(difficalty):
    secret = random.randint(1, difficalty)
    return secret

# - Will prompt the user for a number between 1 to difficulty and return the number.
def get_guess_from_user(diffcalty):
    return int(input(f"Enter a number between 1 and {diffcalty}: "))

# - Will compare the secret generated number to the one prompted by the get_guess_from_user.
def compare_results(guess, secret):
    return guess == secret

# - Will call the functions above and play the game. Will return True / False if the user lost or won.
def play(difficalty):
    secret = generate_number(difficalty)
    guess = get_guess_from_user(difficalty)
    return compare_results(guess, secret)


print(play(4))
