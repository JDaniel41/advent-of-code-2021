import os
from collections import deque

states = []
stateDeque = None

with open(os.path.join(os.path.dirname(__file__), "input2.txt")) as f:
    states = [(int)(val) for val in f.readline().split(',')]
    states.sort()
    filteredStates = []

    highestTimer = max([9])

    stateMap = [0] * highestTimer
    for state in states:
        stateMap[state] += 1
    print(stateMap)

stateDeque = deque(stateMap)
for day in range(1, 257):
    # Decrement States
    stateDeque.rotate(-1)

    day8 = stateDeque.pop()
    day7 = stateDeque.pop()
    day6 = stateDeque.pop()

    stateDeque.append(day8 + day6)
    stateDeque.append(day7)
    stateDeque.append(day8)

    print(f'Day {day}: There are {sum(stateDeque)} lanternfish')
