class Animal:
    """Домашние животные"""
    hungry = 'да'
    weights = []
    names = []

    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight
        self.sound = sound
        Animal.weights.append(weight)
        Animal.names.append(self)

    def feed(self):
        self.hungry = 'нет'


class Ruminants(Animal):
    """Жвачные"""
    need_to_milk = 'да'

    def milk(self):
        self.need_to_milk = 'да'


class Birds(Animal):
    need_collect_eggs = 'да'

    def egg_picking(self):
        self.need_collect_eggs = 'нет'


class Rams(Animal):
    """Семейство баранов"""
    need_cut = 'да'

    def cut(self):
        self.need_cut = 'нет'


goose1 = Birds('Серый', 5, 'кря')
goose2 = Birds('Белый', 5, 'кря')
cow = Ruminants('Манька', 100, 'му')
sheep1 = Rams('Барашек', 20, 'бе')
sheep2 = Rams('Кудрявый', 20, 'бе')
chicken1 = Birds('Ко-ко', 3, 'цып')
chicken2 = Birds('Кукареку', 3, 'цып')
goat1 = Ruminants('Рога', 15, 'ме')
goat2 = Ruminants('Копыта', 10, 'ме')
duck = Birds('Кряква', 5, 'кря')

print(f'Гусь по имени {goose1.name} голоден: {goose1.hungry}, яйца нужно собрать: {goose1.need_collect_eggs}')
print(f'Гусь по имени {goose2.name} голоден: {goose2.hungry}, яйца нужно собрать: {goose2.need_collect_eggs}')
goose1.feed()
goose2.feed()
goose1.egg_picking()
goose2.egg_picking()
print(f'Гусь по имени {goose1.name} голоден: {goose1.hungry}, яйца нужно собрать: {goose1.need_collect_eggs}')
print(f'Гусь по имени {goose2.name} голоден: {goose2.hungry}, яйца нужно собрать: {goose2.need_collect_eggs}')

print(f'Общий вес всех животных = {goose1.weight+goose2.weight+cow.weight+sheep1.weight+sheep2.weight+chicken1.weight+chicken2.weight+goat1.weight+goat2.weight+duck.weight} кг')

for animal in Animal.names:
    if max(Animal.weights) == animal.weight:
       print(f"Самый тяжелый зверь: {animal.name}")