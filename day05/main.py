import os

ventMap = {} # x: [y's]

with open(os.path.join(os.path.dirname(__file__), "input2.txt")) as f:
    for line in f:
        processedLine = line.replace(' -> ', ',')
        numbers = [(int)(val) for val in processedLine.split(',')]
        if numbers[0] != numbers[2] and numbers[1] != numbers[3]:
            print(f'({numbers[0]}, {numbers[1]}) -> ({numbers[2]}, {numbers[3]})')

             # Diagonal
            xCoords = list(range(numbers[0], numbers[2] + 1)) if numbers[2] > numbers[0] else list(range(numbers[2], numbers[0] + 1))
            yCoords = list(range(numbers[1], numbers[3] + 1)) if numbers[3] > numbers[1] else list(range(numbers[3], numbers[1] + 1))
                
            if (xCoords[0], yCoords[0]) != (numbers[0], numbers[1]) and (xCoords[-1], yCoords[-1]) != (numbers[0], numbers[1]):
                xCoords.reverse()

            print(list(zip(xCoords, yCoords)))
            for x, y in zip(xCoords, yCoords):
                if x not in ventMap:
                    ventMap[x] = []
                
                ventMap[x].append(y)
        elif numbers[0] == numbers[2]:
            # Vertical Lines
            if numbers[0] not in ventMap:
                ventMap[numbers[0]] = []
            if numbers[1] < numbers[3]:
                [ventMap[numbers[0]].append(val) for val in range(numbers[1], numbers[3] + 1)]
            else:
                [ventMap[numbers[0]].append(val) for val in range(numbers[3], numbers[1] + 1)]
        else:
            # Horizontal Lines
            if numbers[0] < numbers[2]:
                for val in range(numbers[0], numbers[2] + 1):
                    if val not in ventMap: ventMap[val] = []

                    ventMap[val].append(numbers[1])
            else:
                for val in range(numbers[2], numbers[0] + 1):
                    if val not in ventMap: ventMap[val] = []

                    ventMap[val].append(numbers[1])
    

repetitions = 0
for xCoordinate in ventMap:
    # Count Repeating Vals
    seenVals = set()
    repetitionsVals = set()

    for val in ventMap[xCoordinate]:
        if val in seenVals and val not in repetitionsVals:
            repetitions += 1
            repetitionsVals.add(val)
        else:
            seenVals.add(val)



for key in ventMap:
    print(f'{key}: {ventMap[key]}')

print(f'Repetitions: {repetitions}')