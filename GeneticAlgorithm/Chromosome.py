import random
from GeneticAlgorithm.Constants import Constants

class Chromosome(object):

    __validationFunc = None
    __scoreFunc = None

    def __init__(self, target):
        self.chromo = ""
        for i in range(Constants.chromoLen):
            currPos = len(self.chromo)
            randomNum = random.randint(0, len(Constants.spaceList) - 1)
            binString = "{0:b}".format(randomNum)
            binString = binString.zfill(Constants.bitsLen)
            self.chromo  = self.chromo + binString

    def mutate(self):
        for i in range(self.chromo):
            if random.random <= Constants.mutationRate:
                bit = '0' if self.chromo[i] == '1' else '1'
                self.chromo = self.chromo[:i] + bit + self.chromo[i+1:]


    def crossover(self, otherChromo):

        if random.random() > Constants.crossoverRate:
            return
        pos = random.choice(range(len(self.chromo)))

        restOfMe = self.chromo[pos:]
        frontOfMe = self.chromo[:pos]

        restOfOther = otherChromo.chromo[pos:]
        frontOfOther = otherChromo.chromo[:pos]

        self.chromo = frontOfMe + restOfOther
        otherChromo.chromo = frontOfOther + restOfMe

    def decode(self):
        codes = list(Constants.splitStringByN(self.chromo, Constants.bitsLen))
        decodedCode = list()
        for i in range(len(codes)):
            decodedCode.append(str(int(codes[i],2)))
        decodedCode = "".join(decodedCode)
        return decodedCode

    def scoreChromo(self):
        if Chromosome.__scoreFunc is None:
            print("Score function is not implemented yet!!")
            return
        self.score = Chromosome.__scoreFunc(self.chromo)

    def isValid(self):
        if Chromosome.__validationFunc is None:
            print("Validation func is None")
            return False
        return Chromosome.__validationFunc(self.chromo)

    @staticmethod
    def setScoreFunction(function):
        """
            scoreFunction interface must be like this:

            float function(chromo)
        """
        Chromosome.__scoreFunc = function

    @staticmethod
    def setValidationFunction(function):
        """
            validtaionFunction interface must be like this:

            boolean function(chromo)
        """
        Chromosome.__validationFunc = function
