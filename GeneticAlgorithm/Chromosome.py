import random
from GeneticAlgorithm.Constants import Constants

class Chromosome(object):
    """
        @chrome encoded String for chromosome
        @target expected solution for algorithm (must be numeric)
        @total calculated current value on chromosome
    """
    __validationFunc = None
    __scoreFunc = None

    def __init__(self, target):
        self.chromo = ""
        self.target = target
        self.total = 0
        for i in range(Constants.getChromoLen()):
            currPos = len(self.chromo)
            randomNum = random.randint(0, len(Constants.getSpaceList()) - 1)
            binString = "{0:b}".format(randomNum)
            binString = binString.zfill(Constants.getBitsLen())
            self.chromo  = self.chromo + binString
        self.scoreChromo()

    def mutate(self):
        for i in range(len(self.chromo)):
            if random.random() <= Constants.getMutationRate():
                bit = '0' if self.chromo[i] == '1' else '1'
                self.chromo = self.chromo[:i] + bit + self.chromo[i+1:]


    def crossover(self, otherChromo):

        if random.random() > Constants.getCrossoverRate():
            return
        pos = random.choice(range(len(self.chromo)))

        restOfMe = self.chromo[pos:]
        frontOfMe = self.chromo[:pos]

        restOfOther = otherChromo.chromo[pos:]
        frontOfOther = otherChromo.chromo[:pos]

        self.chromo = frontOfMe + restOfOther
        otherChromo.chromo = frontOfOther + restOfMe

    def decode(self):
        codes = list(Constants.splitStringByN(self.chromo, Constants.getBitsLen()))
        decodedCode = list()
        for i in range(len(codes)):
            index = int(codes[i],2)
            if index < len(Constants.getSpaceList()):
                decodedCode.append(str(Constants.getSpaceList()[index]))
        decodedCode = "".join(decodedCode)
        return decodedCode

    def getConstants(self):
        return Constants;

    def scoreChromo(self):
        assert Chromosome.__scoreFunc is not None, "Score function must be implemented by setScoreFunction method!"
        self.score = Chromosome.__scoreFunc(self)

    def isValid(self):
        assert Chromosome.__validationFunc is not None, "Validation function must be implemented by setValidationFunction method!"
        return Chromosome.__validationFunc(self)

    def __str__(self):
        return self.chromo

    def __repr__(self):
        return self.chromo

    @staticmethod
    def setScoreFunction(function):
        """
            scoreFunction interface must be like this:

            float function(chromosome)
        """
        Chromosome.__scoreFunc = function

    @staticmethod
    def setValidationFunction(function):
        """
            validtaionFunction interface must be like this:

            boolean function(chromosome)
        """
        Chromosome.__validationFunc = function
