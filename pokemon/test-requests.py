import requests
# import pprint
# pp = pprint.PrettyPrinter(depth=2)
import random

'''url = "https://pokeapi.co/api/v2/pokemon/4"
response = requests.get(url)

if response.ok:
    data = response.json()
    st = []
    for item in data['stats']:
        st.append(item['stat']['name'])
    print(st)'''
    
    
    
    
    
    
    
'''url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
response = requests.get(url)

if response.ok:
    data = response.json()
    pokemon = []
    for item in data['results']:
        pokemon.append(item['name'])
    print(pokemon)'''
    
    
    
    
    
    
    
    
'''url = "https://pokeapi.co/api/v2/pokemon/4"
response = requests.get(url)

if response.ok:
    data = response.json()
    info = {
        "name": data['name'],
        "abilities": [ability['ability']['name'] for ability in data['abilities']],
        "id": data['id'],
        "stats": [{stat['stat']['name'], stat['base_stat']} for stat in data['stats']],
        "types": [type['type']['name'] for type in data['types']],
        
    }
    print(info)'''


'''def pokedata(name):
    url = "https://pokeapi.co/api/v2/pokemon/" + name
    response = requests.get(url)
    if response.ok:
        data = response.json()
        info = {
            "name": data['name'],
            "abilities": [ability['ability']['name'] for ability in data['abilities']],
            "id": data['id'],
            "stats": [{stat['stat']['name'], stat['base_stat']} for stat in data['stats']],
            "types": [type['type']['name'] for type in data['types']],
            "species": data['species']
        }
        return info
    else:
        return None'''
    
    
'''url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
response = requests.get(url)

if response.ok:
    data = response.json()
    list = [item['name'] for item in data['results']]
            
    term = input("Enter a pokemon name: ")
    search = [item for item in list if term.lower() in item]
    print(search)
    pokemons = []
    for item in search:
        result = pokedata(item)
        pokemons.append(result)
        
    # pp.pprint(pokemons)
    print(pokemons)        '''

'''def catch():
    url = "https://pokeapi.co/api/v2/pokemon-species/darkrai"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        print("A wild " + data['name'] + " appeared!")
        capture_rate = data['capture_rate']
        random_number = random.randint(1,255)
        print(f"{random_number} <= {capture_rate}")
        if random_number <= capture_rate:
            print(f"You caught {data['name']}!")
        else:
            print(f"{data['name']} escaped!")

catch()'''
    
def evolve():
    url = "https://pokeapi.co/api/v2/pokemon/6"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        if data['chain']['evolves_to']:
            pokemon = print(f"{caught_pokemon['name']} evolved into {data['chain']['evolves_to'][0]['species']['name']}!")
        else:
            print(f"{caught_pokemon['name']} cannot evolve!")
        return pokemon
    
evolve()
    
runs = 5    
while runs > 0:
    id = str(random.randint(1,151))
    url = "https://pokeapi.co/api/v2/pokemon-species/" + id
    response_species = requests.get(url)
    response_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/" + id)
    if response_species.ok and response_pokemon.ok:
        caught_pokemon = []
        data_species = response_species.json()
        data_pokemon = response_pokemon.json()
        print(f"a wild {data_pokemon['name']} appears!")
        print(pokedata(data_pokemon['name']))
        option = input("Would you like to catch it? (y/n) ")
        if option == 'y':
            pokemon = catch(data_pokemon['name'], data_species['capture_rate'])
            if pokemon:
                caught_pokemon.append(pokemon)
                i = 0
                if input("would you like to evolve it? (y/n)") == 'y':
                    caught_pokemon.append(evolve(caught_pokemon[i], data_species))
                    i += 1
                else:
                    print("You ran away!")
        print(caught_pokemon)'''
    


    
    
  
            
        
