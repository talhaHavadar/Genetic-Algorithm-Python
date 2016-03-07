from GeneticAlgorithm.Chromosome import Chromosome
from GeneticAlgorithm.Constants import Constants
import random


class Algorithm:

    def __init__(self, spaceList, chromoLen = 5, mutationRate = .001, crossoverRate = .7, poolSize = 40):
        """
            poolSize must be even
        """
        self.constants = Constants(spaceList = spaceList)
        self.poolSize = poolSize
        self.__setConstants(chromoLen, mutationRate, crossoverRate)

    def __setConstants(self, chromoLen, mutationRate, crossoverRate):
        self.constants.setChromoLen(chromoLen)
        self.constants.setMutationRate(mutationRate)
        self.constants.setCrossingoverRate(crossoverRate)

    def setScoreFunctionForChromo(self, function):
        Chromosome.setScoreFunction(function)

    def setValidationFunctionForChromo(self, function):
        Chromosome.setValidationFunction(function)

    def selectFromPool(self, pool):
        totalScore = 0.0
        for i in reversed(range(0, len(pool), 1)):
            totalScore += pool[i].score
        sliceRnd = totalScore * random.random()
        fTot = 0.0
        for i in reversed(range(0, len(pool), 1)):
            chromo = pool[i]
            fTot += chromo.score
            if fTot >= sliceRnd:
                pool.remove(chromo)
                return chromo
        chromo = pool[-1]
        pool.remove(chromo)
        return chromo

    def solve(self, target):
        self.target = target
        chromosomePool = [Chromosome(target) for x in range(self.poolSize)]
        newPool = list()
        generation = 0
        while True:
            newPool = []
            generation += 1
            for i in reversed(range(0,len(chromosomePool),2)):
                n1 = self.selectFromPool(chromosomePool)
                n2 = self.selectFromPool(chromosomePool)

                # Crossing over and mutation
                n1.crossover(n2)
                n1.mutate()
                n2.mutate()

                n1.scoreChromo()
                n2.scoreChromo()

                # if score is 0 then we reach the target value
                if n1.isValid() and n1.score == 0:
                    print("Total Generation: %s Solution: %s" % (generation, n1.decode()))
                    return {
                        "generationCount": generation,
                        "solution": n1.decode(),
                        "solutionInBinary": n1.chromo
                    }
                if n2.isValid() and n2.score == 0:
                    print("Total Generation: %s Solution: %s" % (generation, n2.decode()))
                    return {
                        "generationCount": generation,
                        "solution": n2.decode(),
                        "solutionInBinary": n2.chromo
                    }
                if n1.isValid():
                    print("Genarations: %s N1= valid: %s score: %s decodedValue: %s" % (generation, n1.isValid(),n1.score, n1.decode()))
                if n2.isValid():
                    print("Genarations: %s N2= valid: %s score: %s decodedValue: %s" % (generation, n2.isValid(),n2.score, n2.decode()))
                newPool.append(n1)
                newPool.append(n2)

            chromosomePool.extend(newPool)
