




class Cell:


    def __init__(self, id, subId):
        self.combos = list(range(1, 10))

        self.id = id
        self.subId = subId

        self.solved = False
        self.newSolution = False
        self.solvedValue = 0

    def setSolution(self, num):
        self.solvedValue = num
        self.combos = [num]

        self.solved = True
    

    def isSolved(self):

        if self.solved:
            return True
        
        elif len(self.combos) == 1:
            self.solvedValue = self.combos[0]
            self.solved = True
            self.newSolution = True
            #print("New Solution")

            return True

        else:
            return False

    def deletePossible(self, num):

        if not self.solved:

            if num in self.combos:
                self.combos.pop(self.combos.index(num))