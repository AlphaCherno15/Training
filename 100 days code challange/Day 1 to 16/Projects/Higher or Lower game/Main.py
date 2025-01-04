from game_data import data
import random as rd
import art

first_choice = rd.choice(data)
second_choice = None

def randon():
    global second_choice
    while True:
        second_choice = rd.choice(data)
        if second_choice != first_choice:
            break
    return second_choice

def game():
    randon()
    score = 0
    name_a = first_choice["name"]
    description_a = first_choice["description"]
    country_a = first_choice["country"]
    follower_a = first_choice["follower_count"]
    while True:
        name_b = second_choice["name"]
        description_b = second_choice["description"]
        country_b = second_choice["country"]
        follower_b = second_choice["follower_count"]
        print(art.logo)
        print(f'Compare A: {name_a}, a {description_a}, from {country_a}')
        print(f'You are right! your score is {score}' if score > 0 else '')
        print(art.vs)
        print(f'Compare A: {name_b}, a {description_b}, from {country_b}')
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if follower_a > follower_b and player_choice == "a":
            score += 1
            # print(f'You are right! your score is {score}')
            name_a = name_b
            description_a = description_b
            country_a = country_b
            follower_a = follower_b
            randon()
        elif follower_a < follower_b and player_choice == "b":
            score += 1
            # print(f'You are right! your score is {score}')
            name_a = name_b
            description_a = description_b
            country_a = country_b
            follower_a = follower_b
            randon()
        else:
            print(f'You are wrong! your total score is {score}')
            break
game()
