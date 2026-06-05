import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokeman_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"API Failed with status code: {response.staus_code}")


pokeman_name = "pikachu"
pokemon_info = get_pokeman_info(pokeman_name)
print(f"Name: {pokemon_info["name"]}")
print(f"id: {pokemon_info["id"]}")
print(f"Height: {pokemon_info["height"]}")
print(f"Weight: {pokemon_info["weight"]}")
