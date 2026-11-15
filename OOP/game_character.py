class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def display(self):
        print("Character Name:", self.name)
        print("Health:", self.health)


class Warrior(Character):
    def attack(self):
        print(self.name, "attacks with a sword!")


class Mage(Character):
    def attack(self):
        print(self.name, "casts a magic spell!")


class Archer(Character):
    def attack(self):
        print(self.name, "shoots an arrow!")


w = Warrior("Warrior", 100)
m = Mage("Mage", 80)
a = Archer("Archer", 90)

w.display()
w.attack()

print()

m.display()
m.attack()

print()

a.display()
a.attack()
