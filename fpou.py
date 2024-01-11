import random

def minmax(value):
    if value <= 0:
        value = 0
    if value >= 100:
        value = 100
    return value

state = {
"name": input("Enter name of your pou: "),
"age": 0,
"hunger": 0,
"energy": 100,
"happiness": 100,
"health": 100,
"alive": True
}

def status():
    print(f"\n\t\t{state['name']} - hunger: {state['hunger']}, energy: {state['energy']}, happiness: {state['happiness']}, health: {state['health']}, age: {state['age']}\n\n")
def play():
    print("\n\t\tヽ(o＾▽＾o)ノ\n\n")
    new_state = dict(state)
    new_state["hunger"] = minmax(state["hunger"] + 10)
    new_state["energy"] = minmax(state["energy"] - 15)
    new_state["happiness"] = minmax(state["happiness"] + 10)
    new_state["health"] = minmax(state["health"] + 5)
    return new_state

def eat():
    print("\n\t\t(๑ᵔ⤙ᵔ๑)\n\n")
    new_state = dict(state)
    new_state["hunger"] = 0
    new_state["energy"] = minmax(state["energy"] + 20)
    new_state["happiness"] = minmax(state["happiness"] + 10)
    return new_state

def sleep():
    print("\n\t\t(。-ω-)zzz\n\n")
    new_state = dict(state)
    new_state["energy"] = 100
    new_state["happiness"] = minmax(state["happiness"] + 15)
    return new_state

def trick():
    print("\n\t\twah!!! (┛✧Д✧))┛彡┻━┻\n\n")
    new_state = dict(state)
    new_state["hunger"] = minmax(state["hunger"] + 10)
    new_state["energy"] = minmax(state["energy"] - 5)
    new_state["happiness"] = minmax(state["happiness"] + 20)
    new_state["health"] = minmax(state["health"] - 5)
    return new_state

def speak():
    print("\n\t\t(o´∀`o) hya!\n\n")
    new_state = dict(state)
    new_state["happiness"] = minmax(state["happiness"] + 10)
    return new_state

while state["alive"]:
    status()
    option = input("what would you like to do with your pou?\n1º play\n2º eat\n3º sleep\n4º trick\n5º speak\n6º quit\n\n Pick: ")
    if option == "1":
        state = play()
    elif option == "2":
        state = eat()
    elif option == "3":
        state = sleep()
    elif option == "4":
        state = trick()
    elif option == "5":
        state = speak()
    elif option == "6":
        break
    else:
        print("Invalid option")
        continue
    state["age"] += 1
    if state["age"] >= 25 or state["health"] <= 0 or state["happiness"] <= 0 or state["energy"] <= 0 or state["hunger"] >= 100:
        state["alive"] = False
        print("Your pou died, GAME OVER")
        break