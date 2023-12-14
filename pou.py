import random

class pou:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(20, 70)
        self.energy = random.randint(20, 70)
        self.happiness = random.randint(20, 70)
        self.health = 100
        self.age = 0
        self.checks = 0
    
    def __str__(self):
        return f"{self.name} - hunger: {self.hunger}, energy: {self.energy}, happiness: {self.happiness}, health: {self.health}, age: {self.age}"
    
    def die(self):
        if self.hunger == 100 or self.energy == 0 or self.happiness == 0 or self.health == 0 or self.age == 10:
            return True
        else:
            return False
        
    def check(self):
        self.checks += 1
        if (self.checks % 5) == 0:
            self.age += 1
        if self.hunger <= 0:
            self.hunger = 0
        if self.energy <= 0:
            self.energy = 0
        if self.happiness <= 0:
            self.happiness = 0
        if self.health <= 0:
            self.health = 0
        if self.hunger >= 100:
            self.hunger = 100
        if self.energy >= 100:
            self.energy = 100
        if self.happiness >= 100:
            self.happiness = 100
        if self.health >= 100:
            self.health = 100
    
    
    def play(self):
        print("\n\t\tヽ(o＾▽＾o)ノ\n\n")
        self.hunger += random.randint(5, 20)
        self.energy -= random.randint(5, 20)
        self.happiness += random.randint(5, 20)
        self.health += random.randint(5, 10)
        self.check()
        
    def eat(self):
        print("\n\t\t(๑ᵔ⤙ᵔ๑)\n\n")
        self.hunger = 0
        self.energy += random.randint(5, 20)
        self.happiness += random.randint(5, 20)
        self.check()
    
    def sleep(self):
        print("\n\t\t(。-ω-)zzz\n\n")
        self.energy = 100
        self.health += random.randint(5, 20)
        self.hunger += random.randint(5, 20)
        self.check()
        
    def trick(self):
        print("\n\t\twah!!! (┛✧Д✧))┛彡┻━┻\n\n")
        self.hunger += random.randint(5, 20)
        self.energy -= random.randint(5, 20)
        self.happiness = 100
        self.check()
    
    def speak(self):
        print("\n\t\t(o´∀`o) hya!\n\n")
        self.check()
        
    

pet = pou(input("Welcome, please create your pou: "))
option = input("\nWhat do you want to do?\n\n 1 - Play\n 2 - Eat\n 3 - Sleep\n 4 - Trick\n 5 - Speak\n 6 - Exit\n\n pick: ")
while option != "6":
    if pet.die():
        print("Your pou has died\n\n\t\tGAME OVER\n\n\t\t (´×ω×`)\n\n")
        break
    if option == "1":
        pet.play()
    elif option == "2":
        pet.eat()
    elif option == "3":
        pet.sleep()
    elif option == "4":
        pet.trick()
    elif option == "5":
        pet.speak()
    else:
        print("Invalid input")
    print(pet)
    option = input("\nWhat do you want to do?\n\n 1 - Play\n 2 - Eat\n 3 - Sleep\n 4 - Trick\n 5 - Speak\n 6 - Exit\n\n pick: ")
