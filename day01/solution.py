import os

# Read from File
depths = []

with open(os.path.join(os.path.dirname(__file__), 'input1.txt')) as f:
    for line in f:
        depths.append((int)(line)) 

# Part 1 Solution
numIncreases = 0
prevMeasurement = None
for line in depths:
    newMeasurement = line
    if prevMeasurement != None and newMeasurement > prevMeasurement:
        numIncreases += 1
    prevMeasurement = newMeasurement


print(f'Part 1: The depth increased {numIncreases} times.')

# Part 2 Solution
numIncreases = 0
windowSums = [0]
prevSum = None

for idx, line in enumerate(depths):
    if idx >= len(depths): break
    windowSums[idx] += line
    if idx > 0: windowSums[idx-1] += line
    if idx > 1: windowSums[idx-2] += line

    windowSums.append(0)

for idx, val in enumerate(windowSums):
    if idx > 0 and val > windowSums[idx - 1]:
        numIncreases += 1


print(f'Part 2: The depth increased {numIncreases} times.')