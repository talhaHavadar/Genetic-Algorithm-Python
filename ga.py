from GeneticAlgorithm.Algorithm import Algorithm
from GeneticAlgorithm.Constants import Constants
from GeneticAlgorithm.Chromosome import Chromosome

solutionSpace = [
    1,2,3,4,5,6,7,8,9,'+','-','*','/'
]
# 3*5/3+5+2*3
algorithm = Algorithm(spaceList=solutionSpace,chromoLen = 11)
def validate(chromo):
    constants = chromo.getConstants()
    decodedChromo = chromo.decode()
    isNum = True

    for i in range(len(decodedChromo)):
        current = decodedChromo[i]
        currentDigit = False
        if current.isdigit():
            currentDigit = True
            current = int(current)
        if current not in [1,2,3,4,5,6,7,8,9,'+','-','*','/']:
            return False
        if isNum is not currentDigit:
            return False
        if i > 0 and current == 0 and decodedChromo[i-1] == "/":
            return False
        isNum = not isNum
    if len(decodedChromo) > 0 and not decodedChromo[-1].isdigit():
        return False

    return True

def score(chromo):
    def addToTotal():
        decodedChromo = chromo.decode()
        localTotal = 0
        ptr = -1
        for i in range(len(decodedChromo)):
            if decodedChromo[i].isdigit():
                localTotal = int(decodedChromo[i])
                ptr = i
                break
        if ptr == -1:
            return 0
        isNum = False
        operator = ' '
        while ptr < len(decodedChromo):
            current = decodedChromo[ptr]
            # Unexpected values
            if current.isdigit() and not isNum:
                ptr += 1
                continue
            if not current.isdigit() and isNum:
                ptr += 1
                continue

            if isNum:
                if not (int(current) == 0 and operator == "/"):
                    toEval = "%s%s%s" % (localTotal, operator, current)
                    localTotal = eval(toEval)
            else:
                operator = current
            ptr += 1
            isNum = not isNum

        return localTotal

    chromo.total = addToTotal()
    if chromo.total == chromo.target:
        return 0
    else:
        return 1.0 / (chromo.target - chromo.total)

def validateTest():
    decodedChromo = "3*5/3+5+2"
    isNum = True

    for i in range(len(decodedChromo)):
        current = decodedChromo[i]
        currentDigit = False
        if current.isdigit():
            currentDigit = True
            current = int(current)
        if current not in [1,2,3,4,5,6,7,8,9,'+','-','*','/']:
            return False
        if isNum is not currentDigit:
            return False
        if i > 0 and current == 0 and decodedChromo[i-1] == "/":
            return False
        isNum = not isNum
        print("isnum: ", isNum, "i: ", i)
    if len(decodedChromo) > 0 and not decodedChromo[-1].isdigit():
        return False

    return True

def scoreTest():
    def addToTotal():
        decodedChromo = "3*5/3"
        localTotal = 0
        ptr = -1
        for i in range(len(decodedChromo)):
            if decodedChromo[i].isdigit():
                localTotal = int(decodedChromo[i])
                ptr = i
                break
        if ptr == -1:
            return 0
        isNum = False
        operator = ' '
        while ptr < len(decodedChromo):
            current = decodedChromo[ptr]
            # Unexpected values
            if current.isdigit() and not isNum:
                ptr += 1
                continue
            if not current.isdigit() and isNum:
                ptr += 1
                continue

            if isNum:
                if not (int(current) == 0 and operator == "/"):
                    toEval = "%s%s%s" % (localTotal, operator, current)
                    localTotal = eval(toEval)
            else:
                operator = current
            ptr += 1
            isNum = not isNum

        return localTotal

    total = addToTotal()
    if total == 5:
        return 0
    else:
        return 1.0 / (5 - total)

algorithm.setScoreFunctionForChromo(score)
algorithm.setValidationFunctionForChromo(validate)
# print(scoreTest())
algorithm.solve(36)
