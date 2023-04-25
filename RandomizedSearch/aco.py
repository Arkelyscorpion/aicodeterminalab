import random

def distance(city1, city2):
    """Return Euclidean distance between two cities"""
    x1, y1 = city1
    x2, y2 = city2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

class Ant:
    def __init__(self, start_city, num_cities, alpha, beta):
        self.alpha = alpha  # pheromone weight
        self.beta = beta  # distance weight
        self.visited_cities = [start_city]  # keep track of visited cities
        self.pheromone_delta = []  # keep track of pheromone deposits
        self.unvisited_cities = list(range(num_cities))
        self.unvisited_cities.remove(start_city)

    def select_next_city(self, pheromone_matrix, distance_matrix):
        """Select the next city to visit based on pheromone and distance"""
        total_pheromone = 0
        for city in self.unvisited_cities:
            total_pheromone += pheromone_matrix[self.visited_cities[-1]][city] ** self.alpha \
                               * (1.0 / distance_matrix[self.visited_cities[-1]][city]) ** self.beta

        # calculate probability of selecting each city
        city_probabilities = []
        for city in self.unvisited_cities:
            pheromone = pheromone_matrix[self.visited_cities[-1]][city]
            distance = distance_matrix[self.visited_cities[-1]][city]
            city_probabilities.append((pheromone ** self.alpha * (1.0 / distance) ** self.beta) / total_pheromone)

        # choose next city based on probabilities
        next_city = random.choices(self.unvisited_cities, weights=city_probabilities)[0]

        # update visited cities and unvisited cities lists
        self.visited_cities.append(next_city)
        self.unvisited_cities.remove(next_city)

        # update pheromone deposit
        self.pheromone_delta.append((self.visited_cities[-2], self.visited_cities[-1]))

    def calculate_tour_length(self, distance_matrix):
        """Calculate the total length of the ant's tour"""
        tour_length = 0
        for i in range(len(self.visited_cities) - 1):
            tour_length += distance_matrix[self.visited_cities[i]][self.visited_cities[i + 1]]
        tour_length += distance_matrix[self.visited_cities[-1]][self.visited_cities[0]]  # return to start city
        return tour_length

def ant_colony_optimization(num_ants, num_iterations, pheromone_matrix, distance_matrix, alpha, beta, rho, q):
    """Run the Ant Colony Optimization algorithm"""
    num_cities = len(distance_matrix)
    best_tour_length = float('inf')
    best_tour = None

    for iteration in range(num_iterations):
        # create ants and run tours
        ants = [Ant(start_city=random.randint(0, num_cities - 1), num_cities=num_cities, alpha=alpha, beta=beta)
                for _ in range(num_ants)]

        for ant in ants:
            for _ in range(num_cities - 1):
                ant.select_next_city(pheromone_matrix, distance_matrix)

            # return to start city and update pheromone deposit
            ant.pheromone_delta.append((ant.visited_cities[-1], ant.visited_cities[0]))
            tour_length = ant.calculate_tour_length(distance_matrix)

            # update best tour
            if tour_length < best_tour_length:
                best_tour_length = tour_length
                best_tour = ant.visited_cities[:]

            # update pheromone matrix
            for i, j in ant.pheromone_delta:
                pheromone_matrix[i][j] += q / tour_length
                pheromone_matrix[j][i] = pheromone_matrix[i][j]

        # evaporate pheromone
        for i in range(num_cities):
            for j in range(num_cities):
                pheromone_matrix[i][j] *= (1 - rho)

    return best_tour+[best_tour[0]], best_tour_length

def main():
    # define problem parameters
    num_cities = 4
    num_ants = 3
    num_iterations = 5
    alpha = 1
    beta = 5
    rho = 0.5
    q = 100

    # create distance matrix
    distance_matrix = [
        [0, 2, 9, 10],
        [2, 0, 6, 4],
        [9, 6, 0, 8],
        [10, 4, 8, 0]
    ]

    # initialize pheromone matrix
    pheromone_matrix = [
        [0.0, 0.5, 0.5, 0.5],
        [0.5, 0.0, 0.5, 0.5],
        [0.5, 0.5, 0.0, 0.5],
        [0.5, 0.5, 0.5, 0.0]
    ]

    # run ant colony optimization algorithm
    best_tour, best_tour_length = ant_colony_optimization(num_ants, num_iterations, pheromone_matrix, distance_matrix, alpha, beta, rho, q)

    # print results
    print("Best tour:", best_tour)
    print("Best tour length:", best_tour_length)

if __name__ == '__main__':
    main()

