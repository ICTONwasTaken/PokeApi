import requests
import json
import random
import sys

#API COLLECTED
url = "https://pokeapi.co/api/v2/pokemon/"
boi = ["pikachu","garchomp","metagross","charizard","arcanine"]
pokerandom = url + boi[random.randrange(0, 5)]

try:
    response = requests.get(pokerandom, timeout=10)
    response.raise_for_status()
    print(response.status_code)
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 404:
        print("Error 404: The Pokemon was not found.")
    else:
        print(f"Other HTTP Error occurred: {e}")
    sys.exit(1)
except requests.exceptions.ConnectionError:
    print("Couldn't connect. Check your internet connection.")
    sys.exit(1)
except requests.exceptions.Timeout:
    print("The request timed out.")
    sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"Something went wrong with the request: {e}")
    sys.exit(1)

pokemon = json.loads(response.content)
ability = pokemon['abilities'][0]['ability']['name'].capitalize()
hidden_ability = pokemon['abilities'][1]['ability']['name'].capitalize()
winner = pokemon['name']
w = 3

print("Who's that Pokemon!")

while True:
    print(f"-He weighs {pokemon["weight"] / 10}kg;")
    print(f"-Is {pokemon["height"] / 10}m tall;")
    print(f"-And has the ability {ability}, and the hidden ability {hidden_ability}!")
    answer = input(f"({w} Chances): ").lower()

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