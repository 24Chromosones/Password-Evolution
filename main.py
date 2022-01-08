import random
import string
import logic

# Initialization
alphabet = string.ascii_letters
alphabet = [letter for letter in alphabet]
password = ""
population_max = 100  # changeable, has to be an even number though
population = []


for character in range(56):
    password += random.choice(alphabet)


class Unit:
    def __init__(self, new, attempt=""):
        self.attempt = attempt
        if new:
            self.attempt = "".join([random.choice(alphabet) for i in password])

    def show_fitness(self):
        self.fitness = logic.similar(self.attempt, password)
        return self.fitness

    def show_attempt(self):
        return self.attempt

    def birth(self, other_parent):
        self.new_attempt = ""
        for i, v in enumerate(self.attempt):
            num = random.randint(1, 10)
            if 1 <= num <= 5:
                self.new_attempt += v
            else:
                self.new_attempt += other_parent.show_attempt()[i]

        return Unit(new=False, attempt=self.new_attempt)

    def mutation(self):
        num = random.randint(1, 100)
        if num == 100:
            index = random.randint(0, len(self.attempt)-1)
            self.attempt = "".join([v if i != index else random.choice(alphabet) for i, v in enumerate([j for j in self.attempt])])


def create_population():
    while len(population) < population_max:
        population.append(Unit(new=True))


def purge():
    global population
    temp = [(i, i.show_fitness()) for i in population]
    middle = (len(population))//2
    temp.sort(key=lambda x: x[1])
    population = [i for i, v in temp[middle::]]


def display_best():
    fitness_list = [(i.show_attempt(), i.show_fitness()) for i in population]
    return max(fitness_list, key=lambda x:x[1])


def main():
    evolutions = 0
    create_population()
    while True:
        purge()
        pairs = logic.pair(population)
        for pair in pairs:
            population.append(pair[0].birth(pair[1]))
        create_population()
        print(display_best())
        if display_best()[1] == 1:
            print(f"Answer found: {display_best()[0]}\nPassword was {password}\nIt took {evolutions} evolutions")
            return
        for unit in population:
            unit.mutation()
        evolutions += 1


main()
