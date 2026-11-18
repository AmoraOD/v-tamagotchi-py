food_list = [(1, 'Suco', 10),
             (2, 'Bolo', 20),
             (3, 'Hamburger', 40),
             (4, 'Milkshake', 20),
             (5, 'Salada', 40)]

actives_list = [
    (1, 'Desenhar', 10),
    (2, 'Jogar', 30),
    (3, 'Estudar', -10),
    (4, 'Conversar', 30)]

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        self.hunger = max(self.hunger - 20, 0)
        print(f"{self.name} foi alimentado!")

    def play(self):
        if self.energy >= 20:
            self.happiness = min(self.happiness + 20, 100)
            self.energy -= 20
            print(f"{self.name} brincou e se divertiu!")
        else:
            print(f"{self.name} está muito cansado para brincar")

    def sleep(self):
        self.energy = min(self.energy + 30, 100)
        self.hunger = min(self.hunger + 10, 100)
        print(f"{self.name} descansou.")

    def actives(self):
        actives = None

        if self.play is True:
            self.actives.append()

    def status(self):
        print(f"\n{self.name}'s status:")
        print(f"Fome: {self.hunger}")
        print(f"Energia: {self.energy}")
        print(f"Diversão: {self.happiness}")

    def time_passes(self):
        self.hunger = min(self.hunger + 5, 100)
        self.energy = max(self.energy - 5, 0)
        self.happiness = max(self.happiness - 5, 0)

        if self.hunger >= 100 or self.energy <= 0 or self.happiness <= 0:
            print(f"\nAh não! {self.name} se sentiu abandonado.")
            print(10*"="+ " GAME OVER " + 10*"=")
            exit()

    def main():
        name = input('Nome para seu animalzinho: ')
        pet = Pet(name)

        while True:
            print("\nOque deseja fazer?")
            print("1. Alimentar")
            print("2. Brincar")
            print("3. Dormir")
            print("4. Ver Status")
            print("5. Sair")

            choices = input("> ")

            if choices == "1":
                pet.feed()
            elif choices == "2":
                pet.play()
            elif choices == "3":
                pet.sleep()
            elif choices == "4":
                pet.status()
            elif choices == "5":
                print("Até logo!!")
                break
            else:
                print("Opção invalida, digite novamente")

            pet.time_passes()

Pet.main()