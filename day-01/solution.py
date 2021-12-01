import os

# Part 1 Solution
with open(os.path.join(os.path.dirname(__file__), 'input1.txt')) as f:
    numIncreases = 0
    prevMeasurement = None
    for line in f:
        newMeasurement = (int)(line)
        if prevMeasurement != None and newMeasurement > prevMeasurement:
            numIncreases += 1
        prevMeasurement = newMeasurement

print(f'Part 1: The depth increased {numIncreases} times.')

# Part 2 Solution
with open(os.path.join(os.path.dirname(__file__), 'input1.txt')) as f:
    numIncreases = 0
    windowSums = [0]
    windowCounts = [0]

    prevSum = None
    for idx, line in enumerate(f):
        windowSums[idx] += (int)(line)
        if idx > 0: windowSums[idx-1] += (int)(line)
        if idx > 1: windowSums[idx-2] += (int)(line)

        windowSums.append(0)
    
    for i in range(3): windowSums.pop()
    
    for idx, val in enumerate(windowSums):
        if idx > 0 and val > windowSums[idx - 1]:
            numIncreases += 1


print(f'Part 2: The depth increased {numIncreases} times.')