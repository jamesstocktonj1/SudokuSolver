from Cell import *
import time
#from Grid import *



grid = [[Cell(0, 0), Cell(1, 0), Cell(2, 0), Cell(3, 1), Cell(4, 1), Cell(5, 1), Cell(6, 2), Cell(7, 2), Cell(8, 2)],
        [Cell(9, 0), Cell(10, 0), Cell(11, 0), Cell(12, 1), Cell(13, 1), Cell(14, 1), Cell(15, 2), Cell(16, 2), Cell(17, 2)],
        [Cell(18, 0), Cell(19, 0), Cell(20, 0), Cell(21, 1), Cell(22, 1), Cell(23, 1), Cell(24, 2), Cell(25, 2), Cell(26, 2)],
        [Cell(27, 3), Cell(28, 3), Cell(29, 3), Cell(30, 4), Cell(31, 4), Cell(32, 4), Cell(33, 5), Cell(34, 5), Cell(35, 5)],
        [Cell(36, 3), Cell(37, 3), Cell(38, 3), Cell(39, 4), Cell(40, 4), Cell(41, 4), Cell(42, 5), Cell(43, 5), Cell(44, 5)],
        [Cell(45, 3), Cell(46, 3), Cell(47, 3), Cell(48, 4), Cell(49, 4), Cell(50, 4), Cell(51, 5), Cell(52, 5), Cell(53, 5)],
        [Cell(54, 6), Cell(55, 6), Cell(56, 6), Cell(57, 7), Cell(58, 7), Cell(59, 7), Cell(60, 8), Cell(61, 8), Cell(62, 8)],
        [Cell(63, 6), Cell(64, 6), Cell(65, 6), Cell(66, 7), Cell(67, 7), Cell(68, 7), Cell(69, 8), Cell(70, 8), Cell(71, 8)],
        [Cell(72, 6), Cell(73, 6), Cell(74, 6), Cell(75, 7), Cell(76, 7), Cell(77, 7), Cell(78, 8), Cell(79, 8), Cell(80, 8)]]

subCells = []

newSolutions = []

"""
subCells = [[grid[0][0], grid[0][1], grid[0][2], grid[1][0], grid[1][1], grid[1][2], grid[2][0], grid[2][1], grid[2][2]],
            [grid[0][3], grid[0][4], grid[0][5], grid[1][3], grid[1][4], grid[1][5], grid[2][3], grid[2][4], grid[2][5]],
            [grid[0][6], grid[0][7], grid[0][8], grid[1][6], grid[1][7], grid[1][8], grid[2][6], grid[2][7], grid[2][8]],
            [grid[3][0], grid[3][1], grid[3][2], grid[4][0], grid[4][1], grid[4][2], grid[5][0], grid[5][1], grid[5][2]],
            [grid[3][3], grid[3][4], grid[3][5], grid[4][3], grid[4][4], grid[4][5], grid[5][3], grid[5][4], grid[5][5]],
            [grid[3][6], grid[3][7], grid[3][8], grid[4][6], grid[4][7], grid[4][8], grid[5][6], grid[5][7], grid[5][8]],
            [grid[6][0], grid[6][1], grid[6][2], grid[7][0], grid[7][1], grid[7][2], grid[8][0], grid[8][1], grid[8][2]],
            [grid[6][3], grid[6][4], grid[6][5], grid[7][3], grid[7][4], grid[7][5], grid[8][3], grid[8][4], grid[8][5]],
            [grid[6][6], grid[6][7], grid[6][8], grid[7][6], grid[7][7], grid[7][8], grid[8][6], grid[8][7], grid[8][8]]]"""

def setupSubCells():

        for r in range(0, 9):

                subCells.append([])

                for c in range(0, 9):
                        subCells[grid[r][c].subId].append(grid[r][c])



def deleteInColumn(columnNum, possibleNum):

        #print("Deleting number " + str(possibleNum) + " from colulmn " + str(columnNum))

        for i in range(0, 9):
                grid[i][columnNum].deletePossible(possibleNum)

def deleteInRow(rowNum, possibleNum):

        #print("Deleting number " + str(possibleNum) + " from row " + str(rowNum))

        for i in range(0, 9):
                grid[rowNum][i].deletePossible(possibleNum)

def deleteInSubCell(subCellNum, possibleNum):

        #print("Deleting number " + str(possibleNum) + " from sub cell " + str(subCellNum))

        for i in range(0, 9):
                subCells[subCellNum][i].deletePossible(possibleNum)



def deleteOptions():

        #iterate through each row
        for r in range(0, 9):
                
                #iterate through each column
                for c in range(0, 9):
                        
                        if grid[r][c].isSolved():
                                deleteInColumn(c, grid[r][c].solvedValue)
                                deleteInRow(r, grid[r][c].solvedValue)
                                deleteInSubCell(grid[r][c].subId, grid[r][c].solvedValue)

def deleteFromNewSolutions():

        for coord in newSolutions:
                
                deleteInRow(coord[0], grid[coord[0]][coord[1]].solvedValue)
                deleteInColumn(coord[1], grid[coord[0]][coord[1]].solvedValue)
                deleteInSubCell(grid[coord[0]][coord[1]].subId, grid[coord[0]][coord[1]].solvedValue)






def checkNewSolutions():
        global newSolutions

        newSolutions = []

        for r in range(0, 9):

                for c in range(0, 9):
                        
                        #if newSolution variabl is flagged then 
                        #print(grid[r][c].combos, end="\t")

                        grid[r][c].isSolved()

                        if grid[r][c].newSolution:
                                print("New Solution at " + str(c) + "," + str(r) + "\t = " + str(grid[r][c].solvedValue))

                                #newSolutions.append(grid[r][c])
                                newSolutions.append([r, c])
                                grid[r][c].newSolution = False
                                


grid[0][0].setSolution(7)
grid[0][1].setSolution(6)
grid[0][2].setSolution(4)
grid[0][3].setSolution(8)
grid[0][7].setSolution(9)

grid[1][2].setSolution(1)
grid[1][5].setSolution(3)
grid[1][6].setSolution(2)
grid[1][8].setSolution(7)

grid[2][2].setSolution(9)

grid[3][0].setSolution(1)
grid[3][1].setSolution(9)
grid[3][2].setSolution(7)
grid[3][4].setSolution(8)
grid[3][7].setSolution(4)
grid[3][8].setSolution(6)

grid[4][3].setSolution(1)
grid[4][4].setSolution(5)
grid[4][5].setSolution(6)

grid[5][0].setSolution(3)
grid[5][1].setSolution(5)
grid[5][4].setSolution(4)
grid[5][6].setSolution(1)
grid[5][7].setSolution(8)
grid[5][8].setSolution(2)

grid[6][6].setSolution(9)

grid[7][0].setSolution(9)
grid[7][2].setSolution(5)
grid[7][3].setSolution(6)
grid[7][6].setSolution(8)

grid[8][1].setSolution(7)
grid[8][5].setSolution(9)
grid[8][6].setSolution(6)
grid[8][7].setSolution(5)
grid[8][8].setSolution(3)



startT = time.time()

setupSubCells()

print("INITIAL PASS")

deleteOptions()
checkNewSolutions()

"""
print("NEW PASS")

deleteFromNewSolutions()
checkNewSolutions()"""


while len(newSolutions) != 0:

        print("NEW PASS")

        deleteFromNewSolutions()
        checkNewSolutions()

        print("New solution lengths " + str(len(newSolutions)))

endT = time.time()


print("Time taken: " + str(endT - startT))
