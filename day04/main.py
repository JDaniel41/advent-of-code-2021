import os

numbersToCall = []
boardData = []

with open(os.path.join(os.path.dirname(__file__), "input2.txt")) as f:
    numbersToCall=[(int)(num) for num in f.readline().strip().split(',')]
    f.readline()

    rowNum = 0
    currentBoard = []
    for line in f: 
        currentRow = [[(int)(val), False] for val in  line.strip().split()]
        if(len(currentRow) != 0): 
            currentBoard.append(currentRow)
            if rowNum == 4:
                boardData.append(currentBoard)
                rowNum = 0
                currentBoard = []
            else:
                rowNum += 1


# Part 1 Solution
def callNumber(boards, number):
    #print(number)
    for board in boards:
        for row in board:
            for val in row:
                if val[0] == number: 
                    val[1] = True

def printAllBoards(boards):
    for board in boards:
        for row in board:
            for space in row:
                print(f'{space}', end='\t')
            print()
        print()

def checkBoard(board):
    winningBoard = False
    
    # Check Rows
    for row in board:
        scoreSum = 0
        for num, state in row: 
            if state == False:
                # Space hasn't been called. no Bingox
                scoreSum = 0
                break
            else:
                # This means the space was called.
                scoreSum += num
        
        if scoreSum != 0:
            returnVal = 0
            for row in board:
                for num, state in row:
                    if not state: returnVal += num
            return returnVal


    for idx in range(0, 5):
        scoreSum = 0
        for row in board:
            num, state = row[idx]
            if state == False:
                scoreSum = 0
                break
            else:
                scoreSum += num
        
        if scoreSum != 0:
            returnVal = 0
            for row in board:
                for num, state in row:
                    if not state: returnVal += num
            return returnVal
            
    return 0

winningBoards = set()
for num in numbersToCall:
    # Go through each board and remove the called numbers
    callNumber(boardData, num)
    score = 0

    # Check if we have a winner. If we do, print the answer.
    for idx, board in enumerate(boardData):
        if idx in winningBoards: continue
        score = checkBoard(board)
        if score != 0:
            winningBoards.add(idx)
            print(f'Score: {score}\tLast Num: {num}\tProduct: {score * num}')

#printAllBoards(boardData)

    
