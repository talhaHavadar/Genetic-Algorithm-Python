class Constants:
    chromoLen = 5
    spaceList = list()
    bitsLen = 0
    mutationRate = .001
    crossoverRate = .7

    def __init__(self, spaceList = None):
        if spaceList is not None:
            Constants.spaceList = spaceList
            self.__generateEncodeBitCount()
        else:
            print("There is no spaceList in __init__ function!!")
    def __generateEncodeBitCount(self):
        if len(Constants.spaceList) > 0:
            Constants.bitsLen = len("{0:b}".format(len(Constants.spaceList)))
        print("SpaceList Length: ", len(Constants.spaceList), "BitsLen: ", Constants.bitsLen)

    @staticmethod
    def splitStringByN(string, n):
        while string:
            yield string[:n]
            string = string[n:]
