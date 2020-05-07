import random


class Individual:
    def __init__(self):
        self.phenotype = 0


class Population:
    def __init__(self):
        num_individuals = random.randrange(50, 100)
        self.individuals = []

        # INIT INDIVIDUALS
        for _ in range(num_individuals):
            self.individuals.append(Individual())

    def remove(self, i):
        self.individuals.remove(i)

    def add(self, i):
        self.individuals.append(i)

class Landscape:
    def __init__(self):
        self.num_populations = 4
        self.populations = []
        self.matrix = []

        # INIT POPULATIONS
        for _ in range(self.num_populations):
            self.populations.append(Population())

        # INIT DISPERSION MATRIX TODO: FIRST COLUMN IS TOO LARGE
        for y in range(self.num_populations):
            row = []
            percent_left = 100
            for x in range(self.num_populations):
                if x == self.num_populations - 1:
                    dispersion = percent_left
                else:
                    dispersion = random.randrange(0, percent_left)
                    percent_left -= dispersion
                row.append(dispersion)
            self.matrix.append(row)

    def dispersion_matrix(self):
        print("    ", end="")
        for i in range(self.num_populations):
            print((i + 1), end=": ")
        print("\n")
        i = 1
        for y in self.matrix:
            print(str(i) + ":" + str(y) + "\n")
            i += 1

    def move(self):



l = Landscape()
l.dispersion_matrix()