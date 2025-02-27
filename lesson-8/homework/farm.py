class animal:
    def __init__(self, name, lifetime, speed, weight, sound):
        self.name = name
        self.lifetime = lifetime
        self.speed = speed
        self.weight = weight
        self.sound = sound

    def __str__(self):
        return f'{self.name} has a lifetime of {self.lifetime}, speed of {self.speed} and weight of {self.weight} and it makes the voise {self.sound}'

    def walk(self):
        return f'{self.name} is walking'

    def run(self):
        return f'{self.name} is running'

    def eat(self):
        return f'{self.name} is eating'

    def sleep(self):
        return f'{self.name} is sleeping'

    def speak(self):
        return f'{self.name} is making the sound {self.sound}'


class dog(animal):
    def __init__(self, name, lifetime, speed, weight, sound, breed):
        super().__init__(name, lifetime, speed, weight, sound)
        self.breed = breed

    def __str__(self):
        return f'{self.name} has a lifetime of {self.lifetime}, speed of {self.speed} and weight of {self.weight} and it makes the voise {self.sound} and it is a {self.breed}'

    def guard(self):
        return f'{self.name} is guarding your house'


class cow(animal):
    def __init__(self, name, lifetime, speed, weight, sound, milk_amount):
        super().__init__(name, lifetime, speed, weight, sound)
        self.milk_amount = milk_amount

    def __str__(self):
        return f'{self.name} has a lifetime of {self.lifetime}, speed of {self.speed} and weight of {self.weight} and it makes the voise {self.sound} and it produces {self.milk_amount} liters of milk'

    def milk(self):
        return f'{self.name} is giving you milk'


class rabbit(animal):
    def __init__(self, name, lifetime, speed, weight, sound, kit):
        super().__init__(name, lifetime, speed, weight, sound)
        self.kit = kit  

    def __str__(self):
        return f'{self.name} has a lifetime of {self.lifetime}, speed of {self.speed} and weight of {self.weight} and it makes the voise {self.sound} and it has {self.kit} babies'


con = input("Welcome to the farm\nEnter any key to continue or 0 to exit: ") 
while con != "0":
    option = input('Enter the animal you want to know about or 0 to exit: ').lower()
    
    if option == "dog":        
        animal_obj = dog('Steve', '10 years', '20 km/h', '10 kg', 'bark', 'bulldog')
    elif option == "cow":
        animal_obj = cow('Molly', '20 years', '10 km/h', '100 kg', 'moo', '10')
    elif option == "rabbit":
        animal_obj = rabbit('Ace', '5 years', '10 km/h', '5 kg', 'squeak', '5')
    elif option == "0":
        break    
    else:
        print("Invalid option")
        continue

    print(animal_obj)

    while True:
        action = input(f"\nChoose an action for {animal_obj.name}: walk, run, eat, sleep, speak" 
                       + (", guard" if isinstance(animal_obj, dog) else "")
                       + (", milk" if isinstance(animal_obj, cow) else "")
                       + " or type 'back' to choose another animal: ").lower()

        if action == "walk":
            print(animal_obj.walk())
        elif action == "run":
            print(animal_obj.run())
        elif action == "eat":
            print(animal_obj.eat())
        elif action == "sleep":
            print(animal_obj.sleep())
        elif action == "speak":
            print(animal_obj.speak())
        elif action == "guard" and isinstance(animal_obj, dog):
            print(animal_obj.guard())
        elif action == "milk" and isinstance(animal_obj, cow):
            print(animal_obj.milk())
        elif action == "back":
            break
        else:
            print("Invalid action")
