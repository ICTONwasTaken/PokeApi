#Poke name
#Poke height
#Poke weight

import requests
import json
import random

#API COLLECTED
url = "https://pokeapi.co/api/v2/pokemon/"
boi = ["pikachu","garchomp","metagross","charizard","arcanine"]
pokerandom = url + boi[random.randrange(0, 5)]

w = 3

response = requests.get(pokerandom)
print(response.status_code)

pokemon = json.loads(response.content)
winner = pokemon['name']

print("Who's that Pokemon!")

while True:
    print("He weighs",pokemon["weight"], "!")
    print("And is" ,pokemon["height"], "tall!")
    answer = input(f"(Chances:{w}) Who is he? ").lower()

    if answer != winner and w != 1:
        print("Beeeeeep, wrong!")
        print("")
        w -= 1
    elif answer != winner and w == 1:
        print("")
        print("Out of chances!")
        print(f"The answer was {winner.capitalize()}. Better luck next time!")
        break
    else:
        print("")
        print(f"Correct! Good job! The answer was {winner.capitalize()}.")
        break