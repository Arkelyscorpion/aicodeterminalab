import random
cities=[0,1,2,3,4]
distances = [
    [0, 2, 3, 5, 6],
    [2, 0, 4, 8, 2],
    [3, 4, 0, 2, 3],
    [5, 8, 2, 0, 1],
    [6, 2, 3, 1, 0]
]
start=0
population_size=50
mutation_rate=0.5
generations=1000
def genetic_algorithm(population_size,mutation_rate,generations,cities,distances,start):
    population=generate_population(population_size,cities,distances,start)
    best_path=population[0]
    for i in range(generations):
        parent1=tournament_selection(population)
        parent2=tournament_selection(population)
        child=crossover(parent1,parent2,start)
        child=mutation(child,mutation_rate)
        population.append(child)
        population=sorted(population,key=lambda x:calculate_distance(x,distances))
        population=population[:population_size]
        if(calculate_distance(population[0],distances)<calculate_distance(best_path,distances)):
           best_path=population[0]
    return best_path
def generate_population(population_size,cities,distances,start):
    res=[]
    for i in range(population_size):
        temp=list(range(len(cities)))
        random.shuffle(temp)
        new_temp=[start]
        for i in temp:
            if i!=start:
                new_temp.append(i)
        new_temp.append(start)
        res.append(new_temp)
    return res
def tournament_selection(population):
    candidates=random.sample(population,3)
    candidates=sorted(candidates,key=lambda x:calculate_distance(x,distances))
    return candidates[0]
def calculate_distance(path,distances):
    cost=0
    for i in range(len(path)-1):
        cost+=distances[path[i]][path[i+1]]
    return cost
def crossover(parent1,parent2,start):
    res=[-1]*(len(parent1))
    res[0]=start
    res[-1]=start
    start=random.randint(1,len(parent1)-2)
    end=random.randint(1,len(parent1)-2)
    if start>end:
        start,end=end,start
    for i in range(start,end):
        res[i]=parent1[i]
    temp=[]
    for i in range(len(parent2)):
        if parent2[i] not in res:
            temp.append(parent2[i])
    j=0
    for i in range(len(res)):
        if res[i]==-1:
            res[i]=temp[j]
            j+=1
    return res
def mutation(path,mutation_rate):
    i=random.randint(1,len(path)-2)
    j=random.randint(1,len(path)-2)
    while random.random()>mutation_rate:
        j=random.randint(1,len(path)-2)
    path[i],path[j]=path[j],path[i]
    return path
best_path=genetic_algorithm(population_size,mutation_rate,generations,cities,distances,start)
print("Best Path:",best_path)
print("Cost:",calculate_distance(best_path,distances))
