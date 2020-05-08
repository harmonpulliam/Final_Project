# IMPORTS
import random
from matplotlib import pyplot as plt


class Individual:
    def __init__(self, phenotype=None):
        """Initializes the phenotype of each individual"""
        self.phenotype = phenotype


class Population:
    def __init__(self, id=1):
        """Initializes id and list of individuals for each population"""
        self.id = id
        self.individuals = []

        # INIT INDIVIDUALS
        num_individuals = random.randrange(50, 100)
        for i in range(num_individuals):
            self.individuals.append(Individual(self.id))  # individual phenotype is the same as the id of the population
            # this way the phenotype is the same between every individual
            # in the population

    def remove(self, i):
        """Removes individuals from a population"""
        self.individuals.remove(i)

    def add(self, i):
        """Adds individuals to a population"""
        self.individuals.append(i)


class Landscape:
    def __init__(self, num_populations):
        """Initializes a list of populations and randomizes a dispersion matrix for the populations"""
        self.num_populations = num_populations
        self.populations = []
        self.matrix = []

        # INIT POPULATIONS
        for i in range(self.num_populations):
            self.populations.append(Population(i + 1))  # i+1 is population id

        # INIT DISPERSION MATRIX
        for y in range(self.num_populations):  # loops through rows of matrix
            row = []  # each row of the matrix is a list
            percent_left = 100  # makes sure that each row of matrix adds up to 100%
            for x in range(self.num_populations):  # loops through the columns of each row
                if x == self.num_populations - 1:  # if at the last row, use the rest of the percentage
                    dispersion = percent_left
                else:
                    if y == x:  # the largest percent goes to staying in the same population
                        dispersion = random.randrange(int(percent_left / 2), percent_left)
                    else:
                        dispersion = random.randrange(0, 15)  # can have up to 15% chance of migrating

                    percent_left -= dispersion  # keep track of percent left

                row.append(dispersion)
            self.matrix.append(row)

    def print_matrix(self):
        """Displays randomized dispersion matrix in terminal output"""
        print("   ", end="")
        for i in range(self.num_populations):
            print(str((i + 1)) + "   ", end="")
        print("\n")
        i = 1
        for y in self.matrix:
            print(str(i) + ":" + str(y) + "\n")
            i += 1

    def move(self):
        """Uses dispersion matrix to determine the chance of every individual migrating"""

        moves = {}  # dictionary to record all movements. can not make the movements while in the for loop,
        # because it will mess up the iteration. Dictionary is used after for loop is completed

        move = 1  # keep track of how many movements are made

        for p in self.populations:  # loop through all populations
            for i in p.individuals:  # loop through each individual
                y_num = 1  # keep track of number of rows

                for y in self.matrix:  # loop through each row in matrix
                    if y_num == p.id:  # look for row that corresponds with the population
                        x_num = 1  # keep track of the columns in that row

                        for x in y:  # loop through the columns in that row
                            chance = random.randrange(0, 100)  # chance that animal will migrate

                            if chance < x:
                                moves[move] = (i, y_num, x_num)  # record the individual, their original population,
                                # and their new population based on matrix
                                move += 1
                                break

                            x_num += 1
                    y_num += 1

        # use dictionary to move items
        for item in moves.items():
            data = item[1]  # first item in items is the number of moves, the second is a
            # tuple containing the data we need

            # Extract data from that tuple
            individual = data[0]
            original = data[1]
            new = data[2]

            if new != original:  # only run these methods if the individual is migrating
                self.populations[new - 1].add(individual)
                self.populations[original - 1].remove(individual)


def main():
    """Simulates movement and graphs it using pyplot"""
    l = Landscape(4)  # construct landscape with 4 populations
    l.print_matrix()  # print dispersion matrix to console

    days = 100  # number of days you would like to simulate
    for _ in range(days):
        l.move()  # run the move method for x amount of days

    population = []  # these list will be used to collect data for pyplot
    size = []

    for p in l.populations:  # loop through every population
        population.append(str(p.id))
        size.append(len(p.individuals))

        phenotypes = {}  # a dictionary that contains the amount of times a phenotype is present in a population
        for i in p.individuals:  # loop through every individual
            if i.phenotype not in phenotypes:
                phenotypes[i.phenotype] = 1
            else:
                phenotypes[i.phenotype] += 1  # tracks how many times a phenotype is present

        phen = []  # these lists will be used to collect data for pyplot
        freq = []
        total_phenotypes = len(p.individuals)  # used to calculate frequency as a percent
        for phenotype, frequency in phenotypes.items():  # loop through the dictionary
            phen.append(str(phenotype))
            freq.append(frequency / total_phenotypes)

        # Graph Phenotypic Frequency for each Population
        plt.title("Frequency of Each Phenotype in Population " + str(p.id) + " After " + str(days) + " Days")
        plt.xlabel("Phenotype")
        plt.ylabel("Frequency")
        plt.bar(phen, freq)
        plt.show()

    # Graph Population Size
    plt.title("Size of Each Population After " + str(days) + " Days")
    plt.xlabel("Population")
    plt.ylabel("Size")
    plt.bar(population, size)
    plt.show()


main()

# QUESTIONS AND ANSWERS:
"""
How do the frequencies of phenotypes change in each population week-by-week as
individuals move?
    -This depends on the dispersion matrix. If the animals disperse evenly, 
    -then the phenotypes will randomly begin to disperse throughout the landscape.
    -If the dispersion matrix is not even, certain phenotypes will begin to pool
    -into different populations. This affects the population size by creating one
    -large population and several small ones. 
    
What effect does an overall increase in the rate of movement (migration) have?
    -Increasing the rate of migration causes the frequencies to evenly distribute 
    -throughout the landscape faster

What happens to both phenotype frequencies and population sizes when movement
probabilities are not symmetric (individuals have a higher probability of
moving from population A to population B, than they do of moving from
population B to population A)?
    -Individuals will eventually begin to 'pool' towards one population, 
    -leaving the other populations to be much smaller
    
What effect does changing the starting population sizes have on the trajectory of
phenotype frequencies? In other words, what might happen if you connect big
habitat patches versus small habitat patches?
    -It takes large populations longer to become 'heterogenized'. This means that 
    -the frequency of phenotypes will will change at a slower rate.
"""
