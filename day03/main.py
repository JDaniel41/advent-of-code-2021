import os

data = []

with open(os.path.join(os.path.dirname(__file__), "input2.txt")) as f:
    for line in f: data.append(line.strip())

def binaryToDecimal(binaryArray):
    returnVal = 0

    for idx, var in enumerate(binaryArray):
        if var == 1:
            returnVal += 2 ** (len(binaryArray) - idx - 1)

    return returnVal

# Part 1 Solution
epsilonDecimal = 0
gammaDecimal = 0
epsilonBinary = []
gammaBinary = []
bitCounts = []
numBits = 0
binaryNum = []
decimalNum = 0

for num in data:
    for idx, byte in enumerate(num):
        if idx == numBits: 
            bitCounts.append([0, 0])
            numBits += 1
        bitCounts[idx][(int)(byte)] += 1

for count0, count1 in bitCounts:
    if count0 > count1:
        epsilonBinary.append(0)
        gammaBinary.append(1)
    else:
        epsilonBinary.append(1)
        gammaBinary.append(0)

epsilonDecimal = binaryToDecimal(epsilonBinary)
gammaDecimal = binaryToDecimal(gammaBinary)

print(f'Epsilon: {epsilonDecimal}\tGamma: {gammaDecimal}\tProduct: {epsilonDecimal * gammaDecimal}')

# Part 2 Solution
oxygenGeneratorData = data.copy()
CO2Data = data.copy()

def getFilteredList(unfilteredList, bitToKeep, bitPos):
    filteredList = []
    for val in unfilteredList:
        if (int)(val[bitPos]) == bitToKeep: filteredList.append(val)
    return filteredList

def getRemainingNum(unfilteredData, bitKeepFunction):
    for idx in range(0, numBits):
        # Get the Most Common Bit
        bitCounts = [0, 0]
        for num in unfilteredData:
            for idx2, byte in enumerate(num):
                if idx == idx2: bitCounts[(int)(byte)] += 1
        
        # Get most common bit
        mostCommonBit = 1 if (bitCounts[0] < bitCounts[1]) else 0

        # Filter out everyone without the bit
        unfilteredData = getFilteredList(unfilteredData, bitKeepFunction(bitCounts), idx)
        if len(unfilteredData) == 1: break

    return [(int)(character) for character in unfilteredData[0]]

CO2ScrubberNum = binaryToDecimal(getRemainingNum(CO2Data, lambda bitCounts : 1 if (bitCounts[0] > bitCounts[1]) else 0))
oxGenNum = binaryToDecimal(getRemainingNum(oxygenGeneratorData, lambda bitCounts : 1 if (bitCounts[0] <= bitCounts[1]) else 0))

print(f'Oxygen: {oxGenNum}\tCO2: {CO2ScrubberNum}\tProduct: {oxGenNum * CO2ScrubberNum}')