import random
import copy

class SudokuGA:
    def __init__(self, puzzle, population_size=100, mutation_rate=0.1, generations=1000):
        self.puzzle = puzzle
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.size = 9
        self.subgrid_size = 3
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = self.create_individual()
            population.append(individual)
        return population

    def create_individual(self):
        individual = []
        for row in range(self.size):
            nums = set(range(1, self.size + 1))
            fixed = []
            for col in range(self.size):
                if self.puzzle[row][col] != 0:
                    fixed.append(self.puzzle[row][col])
                    nums.remove(self.puzzle[row][col])
                else:
                    fixed.append(0)
            for col in range(self.size):
                if fixed[col] == 0:
                    n = random.choice(list(nums))
                    fixed[col] = n
                    nums.remove(n)
            individual.append(fixed)
        return individual

    def fitness(self, individual):
        score = 0
        # Column conflicts
        for col in range(self.size):
            col_values = [individual[row][col] for row in range(self.size)]
            score += (self.size - len(set(col_values)))
        # Subgrid conflicts
        for box_row in range(0, self.size, self.subgrid_size):
            for box_col in range(0, self.size, self.subgrid_size):
                values = []
                for i in range(self.subgrid_size):
                    for j in range(self.subgrid_size):
                        values.append(individual[box_row + i][box_col + j])
                score += (self.size - len(set(values)))
        return score

    def selection(self, ranked_population):
        selected = []
        for _ in range(self.population_size):
            i, j = random.sample(range(len(ranked_population)), 2)
            winner = ranked_population[i] if ranked_population[i][1] < ranked_population[j][1] else ranked_population[j]
            selected.append(winner[0])
        return selected

    def crossover(self, parent1, parent2):
        child = []
        for i in range(self.size):
            if random.random() < 0.5:
                child.append(copy.deepcopy(parent1[i]))
            else:
                child.append(copy.deepcopy(parent2[i]))
        return child

    def mutate(self, individual):
        for row in range(self.size):
            if random.random() < self.mutation_rate:
                indices = [i for i in range(self.size) if self.puzzle[row][i] == 0]
                if len(indices) >= 2:
                    i1, i2 = random.sample(indices, 2)
                    individual[row][i1], individual[row][i2] = individual[row][i2], individual[row][i1]

def print_sudoku(grid):
    for i, row in enumerate(grid):
        print(" ".join(str(val) for val in row))
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

def solve():
    # Sample Puzzle (0 represents blank cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    ga = SudokuGA(puzzle)
    for generation in range(ga.generations):
        ranked_population = sorted(
            [(ind, ga.fitness(ind)) for ind in ga.population],
            key=lambda x: x[1]
        )
        best_individual = ranked_population[0][0]
        best_fitness = ranked_population[0][1]

        if best_fitness == 0:
            print("\n✅ Sudoku Solved:")
            print_sudoku(best_individual)
            return

        selected = ga.selection(ranked_population)
        next_generation = []
        for i in range(0, ga.population_size, 2):
            parent1 = selected[i]
            parent2 = selected[i+1 if i+1 < ga.population_size else 0]
            child1 = ga.crossover(parent1, parent2)
            child2 = ga.crossover(parent2, parent1)
            ga.mutate(child1)
            ga.mutate(child2)
            next_generation.extend([child1, child2])
        ga.population = next_generation[:ga.population_size]

    print("\n❌ No solution found within generation limit.")
    print("Best Attempt:")
    print_sudoku(best_individual)

if __name__ == "__main__":
    solve()