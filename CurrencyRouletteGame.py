import random
import requests
# self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"  # Example API endpoint
def generate_number():
    return random.randint(1, 101)

def get_currency_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url, verify=False)
    print(f'response is {response}')
    return response.json()['rates']['ILS']

def get_monny_interval(difficulty, amount_in_usd):
    print(f'random number is {amount_in_usd}')
    amount_in_usd = generate_number()
    rate = get_currency_rate()
    ils = rate * amount_in_usd
    offset = 5 - difficulty
    return ils - offset, ils + offset
def get_guess_from_user(amount_in_usd):
    guess_money = (int(input(f"How much are {amount_in_usd} USD value in ILS:")))
    return guess_money
def compare_results(min_interval, gess, max_interval):
    comp = (min_interval <= gess <= max_interval)
    print(comp)
    if comp:
        print("You win the game")
    else:
        print("You lost the game")

def play(difficulty):
    amount_in_usd = generate_number()
    min_interval, max_interval = get_monny_interval(difficulty, amount_in_usd)
    print(f'min interval is {min_interval}, max_interval is {max_interval}')
    gess = get_guess_from_user(amount_in_usd)
    print(gess)
    compare_results(min_interval, gess, max_interval)

play(3)

# def get_guess_from_user():
#     guess_money = (int(input(f"What is your guess amount of money:")))
#     return guess_money
#
#
# def compare_results(gen_money, low_money, high_money):
#     comp = (low_money <= gen_money <= high_money)
#     print(comp)
#     if comp:
#         print("You win the game")
#     else:
#         print("You lost the game")
#
#
# def play(difficulty):
#     gen_money = generate_money()
#     print(gen_money)
#     total_money = get_guess_from_user()
#     print(total_money)
#     print(get_money_interval(total_money, difficulty))
#     money_int = get_money_interval(total_money, difficulty)
#     low_money, high_money = money_int
#     print(low_money)
#     print(high_money)
#     compare_results(gen_money, low_money, high_money)
#
# # play(3)
#
# #     x = generate_sequence(difficulty)
# #     print(x)
# #     y = get_guess_from_user(difficulty)
# #     print(y)
# #     compare_results(x, y)
