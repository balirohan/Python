# How to connect to an API using Python

import requests, json

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "Bulbasaur"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    # print(pokemon_info.keys())
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}ft")
    print(f"Weight: {pokemon_info["weight"]}kg")