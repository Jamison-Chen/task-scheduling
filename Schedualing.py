from pip._internal.utils import temp_dir


class SchedualSystem:
    def __sumList(self, aList):
        sum = 0
        for each in aList:
            sum += each
        return sum

    def __init__(self):
        self.__task = []
        self.__numberOfMachine = 0
        self.__factoryList = []
        self.__timeLimit = 0

    def setTimeLimit(self, taskStringShowed):
        self.__timeLimit = taskStringShowed

    def setMachineNumberLimit(self, n):
        self.__numberOfMachine = n

    def assignTasks(self, string):
        self.__task = string.split(",")
        for i in range(len(self.__task)):
            self.__task[i] = int(self.__task[i].strip())
        self.__task.sort(reverse=True)  # large number first

    def __createFactoryList(self, n):
        self.__factoryList.clear()
        for i in range(n):
            self.__factoryList.append([])

    def __LPTAssign(self):
        # LPT stand for "Longest Processing Time First"
        for each in self.__task:
            leastLoads = self.__sumList(self.__factoryList[0])
            leastLoadedMachine = 0
            for i in range(1, len(self.__factoryList)):
                temp = self.__sumList(self.__factoryList[i])
                if temp < leastLoads:
                    leastLoads = temp
                    leastLoadedMachine = i
            self.__factoryList[leastLoadedMachine].append(each)

    def __countMaxTime(self):
        max = 0
        for i in range(len(self.__factoryList)):
            temp = self.__sumList(self.__factoryList[i])
            if temp >= max:
                max = temp
        return max

    def minMachineRequired(self):
        hasSolution = False
        for i in range(1, self.__numberOfMachine+1):
            self.__createFactoryList(i)
            self.__LPTAssign()
            if self.__countMaxTime() <= self.__timeLimit:
                hasSolution = True
                return i
        if not hasSolution:
            return -1

    def resultMessage(self):
        message = "---------------------------------------\n"
        if self.minMachineRequired() != -1:
            for i in range(len(self.__factoryList)):
                message += "Machine" + str(i+1) + ": " + str(self.__factoryList[i]) + \
                    "\tTotal: " + \
                    str(self.__sumList(self.__factoryList[i])) + " (hr)\n"
        else:
            message += "Factroy Overwhelmmed...\n"
        message += "---------------------------------------\n"
        return message
# s = SchedualSystem()
# s.assignTasks("1,8,3,6,7,4,8,4,2,3,1,5,3,1,1")
# s.__createFactoryList(3)
# s.__LPTAssign()
# s.__LPTAssign()
# print(s.resultMessage())
