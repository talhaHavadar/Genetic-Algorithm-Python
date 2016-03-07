from GeneticAlgorithm.Constants import Constants
from GeneticAlgorithm.Chromosome import Chromosome

space = [1, 2, 3, 4, 5, 6, 7, 8, 9]
consts = Constants(spaceList = space)


print(list(Constants.splitStringByN("123456789", 3)))
chromo1 = Chromosome(21)

def Validation(chromo):
    return True

def score(chromo):
    return 100

Chromosome.setValidationFunction(Validation)
Chromosome.setScoreFunction(score)
# chromo2 = Chromosome(21)
# print(chromo1.decode())
# print(chromo2.decode())
#
# print("After crossing over")
# chromo1.crossover(chromo2)
#
# print(chromo1.decode())
# print(chromo2.decode())
chromo = '011101010'

i = 6

bit = '0' if chromo[i] == '1' else '1'
print("bit", bit)
chromo = chromo[:i] + bit + chromo[i+1:]
print (chromo)
