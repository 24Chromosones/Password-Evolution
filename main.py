import random
import string
import logic
import pandas as pd
import plotly.express as px

# Initialization
alphabet = string.ascii_letters
alphabet = [letter for letter in alphabet]
password = ""
password_length = 76  # default 56
population_max = 1000  # changeable
population = []

# Creating password
for character in range(password_length):
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

    def birth(self, other_parent):  # reproduction code
        self.new_attempt = ""
        for i, pw in enumerate(self.attempt):
            num = random.randint(1, 10)
            if 1 <= num <= 5:
                self.new_attempt += pw
            else:
                self.new_attempt += other_parent.show_attempt()[i]

        return Unit(new=False, attempt=self.new_attempt)

    def mutation(self):  # mutation code
        num = random.randint(1, 100)
        if num == 100:
            index = random.randint(0, len(self.attempt)-1)
            self.attempt = "".join([v if i != index else random.choice(alphabet) for i, v in enumerate([j for j in self.attempt])])


def create_population():  # creates new random units
    while len(population) < population_max:
        population.append(Unit(new=True))


def purge():  # purges bottom 50%
    global population
    temp = [(unit, unit.show_fitness()) for unit in population]
    middle = (len(population))//2
    temp.sort(key=lambda x: x[1])
    population = [i for i, v in temp[middle::]]


def display_best(pop):  # displays the best unit
    fitness_list = [(i.show_attempt(), i.show_fitness()) for i in pop]
    return max(fitness_list, key=lambda x: x[1]) # returns the best attempt based on the max i.show_fitness


def main():  # main loop
    evolutions = 0
    total_population = []
    create_population()
    while True:
        evolutions += 1
        for unit in population:
            unit.mutation()
        purge()
        pairs = logic.pair(population)
        for pair in pairs:
            population.append(pair[0].birth(pair[1]))
        total_population.append(population)
        print(display_best(population))
        if display_best(population)[1] == 1:
            print(f"Answer found: {display_best(population)[0]}\nPassword was {password}\nIt took {evolutions} evolutions")
            return total_population
        create_population()

if __name__ == "__main__":
    test = main()
    df = pd.DataFrame(
        {
            'Population': [pop for pop in test],
            'FitList': [[unit.show_fitness() for unit in pop] for pop in test],
            'Best': [display_best(i)[1] for i in test],
            "Frames": range(len(test))
        }
    )
    df = df.explode(column=['Population', "FitList"])
    print(df)
    fig = px.histogram(df, x='FitList', animation_frame="Frames", nbins=15, range_x=(0,1), range_y=(0,750))
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
    fig.show()
