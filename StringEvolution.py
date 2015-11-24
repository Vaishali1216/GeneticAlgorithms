import string
import random
target_string = 'Python'

class individual:
	chromosome=""
	fitness=0

	def __init__(self,chromosome,fitness):
		self.chromosome = chromosome
		self.fitness = fitness
	
	def calculate_fitness(self,target_string):
		if(len(self.chromosome) != len(target_string)):
			print("Error:Length of strings dont match")
			return -1
		counter_fitness=0
		for i,c in enumrate(target_string):
			if(self.chromosome[i]==c):
				counter_fitness+=1
		self.fitness = counter_fitness
		return 1

	def print_chromosome(self):
		print(self.chromosome)


population=[]
for i in range(0,100):
	x = individual(''.join(random.choice(string.ascii_letters) for i in range(len(target_string))),0)
	population.append(x)
for i in population:
	i.print_chromosome()
