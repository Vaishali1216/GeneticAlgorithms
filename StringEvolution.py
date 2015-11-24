import string
import random
target_string = 'HelloWorld'
population=[]
population_size = 100
mutation_rate = 2

class individual:
	fitness=0
	chromosome=""

	def __init__(self,chromosome,fitness):
		self.chromosome = chromosome
		self.fitness = fitness
	
	def calculate_fitness(self,target_string):
		if(len(self.chromosome) != len(target_string)):
			print("Error:Length of strings dont match")
			return -1
		counter_fitness=0
		for i,c in enumerate(target_string):
			if(self.chromosome[i]==c):
				counter_fitness+=1
		self.fitness = counter_fitness
		return 1

	def print_chromosome(self):
		print(self.chromosome)

	def sorting_parameter(a,b):
		return cmp(a.fitness,b.fitness)

	def mutate(self):
		mutated_chromosome=""
		for c in self.chromosome:
			if(random.randint(0,100)<mutation_rate):
				mutated_chromosome+=random.choice(string.ascii_letters)
			else:
				mutated_chromosome+=c
		self.chromosome = mutated_chromosome

def tournament_selection(population,k):
	best = None 
	for i in range(1,k):
		individual = random.choice(population)
		if (best is None) or (individual.fitness > best.fitness) :
			best = individual
	return best

def cross_over(a,b):
	cross_over_point = random.randint(1,len(target_string)-2)
	temp1 = a.chromosome[0:cross_over_point]+b.chromosome[cross_over_point:]
	temp2 = b.chromosome[0:cross_over_point]+a.chromosome[cross_over_point:]
	return individual(temp1,0),individual(temp2,0)





for i in range(0,population_size):
	x = individual(''.join(random.choice(string.ascii_letters) for i in range(len(target_string))),0)
	population.append(x)
for i in population:
	i.calculate_fitness(target_string)
population.sort(individual.sorting_parameter)
# for i in population:
# 	print(i.chromosome,i.fitness)
# population[0].print_chromosome()
# population[1].print_chromosome()
# x,y = cross_over(population[0],population[1])
# x.print_chromosome()
# y.print_chromosome()
generation=0
while(1):
	child_population=[]
	for i in range(45):
		parent1 = tournament_selection(population,2)
		parent2 = tournament_selection(population,2)
		child1, child2 = cross_over(parent1,parent2)
		child1.mutate()
		child2.mutate()
		child1.calculate_fitness(target_string)
		child2.calculate_fitness(target_string)
		child_population.append(child1)
		child_population.append(child2)
	for i in range(90,100):
		child_population.append(population[i])
	
	population = child_population
	population.sort(individual.sorting_parameter)
	generation +=1 
	print(generation,population[99].chromosome)
	if population[99].fitness == len(target_string):
		break



