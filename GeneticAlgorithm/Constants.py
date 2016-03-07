class Constants:
    __chromoLen = 5
    __spaceList = list()
    __bitsLen = 0 # Will be generated automatically
    __mutationRate = .001
    __crossoverRate = .7

    def __init__(self, spaceList = None):
        if spaceList is not None:
            Constants.__spaceList = spaceList
            self.__generateEncodeBitCount()
        else:
            print("There is no spaceList in __init__ function!!")

    def __generateEncodeBitCount(self):
        if len(Constants.__spaceList) > 0:
            Constants.__bitsLen = len("{0:b}".format(len(Constants.__spaceList)))
        print("SpaceList Length: ", len(Constants.__spaceList), "BitsLen: ", Constants.__bitsLen)

    def setSolutionSpace(self, list):
        assert list is not None, "List value must not be None."
        Constants.__spaceList = spaceList
        self.__generateEncodeBitCount()

    def setMutationRate(self, rate):
        assert rate is not None, "Rate value must not be None."
        Constants.__mutationRate = rate

    def setChromoLen(self, chromoLen):
        assert chromoLen is not None, "Chromolen value must not be None."
        Constants.__chromoLen = chromoLen

    def setCrossingoverRate(self, rate):
        assert rate is not None, "Rate value must not be None."
        Constants.__crossoverRate = rate


    @staticmethod
    def getChromoLen():
        return Constants.__chromoLen

    @staticmethod
    def getCrossoverRate():
        return Constants.__crossoverRate

    @staticmethod
    def getMutationRate():
        return Constants.__mutationRate

    @staticmethod
    def getBitsLen():
        return Constants.__bitsLen

    @staticmethod
    def getSpaceList():
        return Constants.__spaceList

    @staticmethod
    def splitStringByN(string, n):
        while string:
            yield string[:n]
            string = string[n:]
