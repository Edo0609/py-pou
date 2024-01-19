import requests
import random

def species(pokemon):
    url = pokemon['species']['url']
    response = requests.get(url)
    if response.ok:
        data = response.json()
        return data

def catch(pokemon):
    species_data = species(pokemon)
    random_number = random.randint(1, 255)
    capture_rate = species_data['capture_rate']
    tries = 1
    while tries < 5:
        if random_number <= capture_rate:
            print(f"You caught {pokemon['name']}!")
            return pokemon
        else:
            if random.randint(1, 100) <= 50:
                print(f"{pokemon['name']} escaped!")
                return None
            else:
                print(f"{pokemon['name']} still wants to fight!")
                tries += 1
    return None

def random_encounter(team):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(random.randint(1, 151))
    new_team = new_team.append(team)
    response = requests.get(url)
    if response.ok:
        data = response.json()
        print(f"A wild {data['name']} appeared!")
        choice = input("What will you do? (1. Catch, 2. Run) ")
        if choice == "1":
            pokemon = catch(data)
            if catch(data):
                new_team.append(pokemon)
                return new_team
        elif choice == "2":
            return new_team
        else:
            print("Invalid choice. Try again.")
    
def get_info(name):
    url = "https://pokeapi.co/api/v2/pokemon/" + name
    response = requests.get(url)
    if response.ok:
        data = response.json()
        info = {
            "name": data['name'],
            "id": data['id'],
            "abilities": [item['ability']['name'] for item in data['abilities']],
            "stats": [{stat['stat']['name'], stat['base_stat']} for stat in data['stats']],
            "types": [type['type']['name'] for type in data['types']],
        }
        print(info)
        
def evo_chain(data):
    url = data['evolution_chain']['url']
    response = requests.get(url)
    if response.ok:
        data = response.json()
    return data

def evolve(name):
    url = "https://pokeapi.co/api/v2/pokemon-species/" + name
    response = requests.get(url)
    if response.ok:
        data = evo_chain(response.json())
    data = "Keep building!"
        

def start_game():
    team = []
    choice = input("What will you do? (1. Search for Pokemon, 2. View Team, 3. Evolve a Pokemon, 4. Exit) ")
    if choice == "1":
        team = random_encounter(team)
    elif choice == "2":
        print(team)
        choice = input ("Would you like to see info of a Pokemon? (1. Yes, 2. No) ")
        if choice == "1":
            print(team)
            name = input("Which Pokemon? ")
            if name in team:
                get_info(name)
            else:
                print("Pokemon not in team. Try again.")
    elif choice == "3":
        name = input("Which Pokemon? ")
        evolve(name)
    elif choice == "4":
        print("Goodbye! Thanks for playing!")
        print("Your final team was:" + team)
        return

def gameloop():
    while True:
        print("Welcome to Pokemon")
        print("1. Play")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            start_game()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")