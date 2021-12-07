import os

startingPos = []

with open(os.path.join(os.path.dirname(__file__), "input2.txt")) as f:
    startingPos = [(int)(val) for val in f.readline().split(',')]

startingPos.sort()
print(startingPos)

currentTarget = None
minCost = None


def getCostForChange(currentPos, target):
    totalCost = 0
    distanceToTravel = abs(currentPos - target)
    for i in range(0, distanceToTravel + 1):
        totalCost += i
    return totalCost

def getCost(currentPositions, currentTarget):
    fuel = 0
    for crab in currentPositions:
        fuel += getCostForChange(crab, currentTarget)
    return fuel

for i in range(startingPos[0], startingPos[-1] + 1):
    # Get the current cost for our current target
    currentCost = getCost(startingPos, i)

    if minCost == None or currentCost < minCost :
        minCost = currentCost

print(minCost)