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
                    if y == x:
                        dispersion = random.randrange(75, percent_left)
                    else:
                        dispersion = random.randrange(0, 15) #TODO: SHIT NOT WORKING OVER 21

                    percent_left -= dispersion
                row.append(dispersion)
            self.matrix.append(row)

    def print_matrix(self):
        print("  "),
        for i in range(self.num_populations):
            print(str((i + 1)) + " "),
        print("\n")
        i = 1
        for y in self.matrix:
            print(str(i) + ":" + str(y) + "\n")
            i += 1

    def move(self):
        pop = 1
        moves = {}
        for p in self.populations:
            for i in p.individuals:
                y_num = 1
                for y in self.matrix:
                    if y_num == pop:
                        x_num = 1
                        for x in y:
                            if x_num != pop:
                                chance = random.randrange(0, 100)
                                if chance < x:
                                    moves[i] = (x_num, y_num)
                            x_num += 1
                    y_num += 1
            pop += 1

        for p in self.populations:
            for i in p.individuals:
                print(moves[i]) #TODO: ERROR

l = Landscape()
l.print_matrix()
l.move()