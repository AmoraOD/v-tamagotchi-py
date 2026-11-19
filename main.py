skills_list = [
    (1, 'Inteligência', 0),
    (2, 'Ginástica', 0),
    (3, 'Cozinha', 0),
    (4, 'Social', 0)
]

food_list = [
    (1, 'Suco', 10),
    (2, 'Bolo', 20),
    (3, 'Hamburger', 40),
    (4, 'Milkshake', 20),
    (5, 'Salada', 40)
]

actives_list = [
    (1, 'Desenhar', 10, 5),
    (2, 'Jogar', 30, 5),
    (3, 'Estudar', -10, -15),
    (4, 'Conversar', 30, 10),
    (5, 'Exercicio', 30, -20)
]

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        f = self._choice(food_list, f"O que {self.name} irá comer?")

        if f is None:
            return

        _, food_name, value = f
        self.hunger = max(self.hunger - value, 0)
        print(f"\n{self.name} comeu {food_name}")
        print(f"Fome -{value}")

    def play(self):
        item = self._choice(actives_list, "Atividades -")
        if item is None:
            return

        _, active_name, happiness_d, energy_d = item

        if energy_d < 0 and self.energy < abs(energy_d):
            print(f"\n{self.name} está muito cansado para {active_name.lower()}!")
            return

        self.happiness = max(0, min(self.happiness + happiness_d, 100))
        self.energy   = max(0, min(self.energy + energy_d, 100))

        print(f"{self.name} começou '{active_name}'! " 
              f"\n(Diversão {happiness_d:+}, Energia {energy_d:+})")

    def sleep(self):
        self.energy = min(self.energy + 30, 100)
        self.hunger = min(self.hunger + 10, 100)
        print(f"\n{self.name} descansou.")

    def _choice(self, items, title):
        print(f"\n{title}")
        
        for item in items:
            print("  ", end="")
            print(" | ".join(str(x) for x in item))

        try:
            choice = int(input("> "))
        except ValueError:
            print("Número invalido, digite novamente")
            return None

        for item in items:
            if item[0] == choice:
                return item

        print("\nOpção invalida!")
        return None

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

    @staticmethod
    def main():
        name = input('Nome para seu animalzinho: ')
        pet = Pet(name)

        while True:
            print("\nOque deseja fazer?")
            print("1. Alimentar")
            print("2. Diversão")
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
                print("\nOpção invalida, digite novamente")
                continue

            pet.time_passes()

Pet.main()