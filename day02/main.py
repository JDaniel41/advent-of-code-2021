import os

commands = []

with open('input2.txt') as f:
    for line in f:
        commands.append(line.strip().split())

# Part 1 Solution
horizontal = 0
depth = 0

for command in commands:
    if command[0] == 'forward':
        horizontal += (int)(command[1])
    elif command[0] == 'down':
        depth += (int)(command[1])
    else:
        depth -= (int)(command[1])

print(f'Horizontal: {horizontal}\tDepth: {depth} ')
print(f'Product: {depth * horizontal}')

# Part 2 Solution
aim = 0
horizontal = 0
depth = 0

for command in commands:
    if command[0] == 'forward':
        horizontal += (int)(command[1])
        depth += aim * (int)(command[1])
    elif command[0] == 'down':
        aim += (int)(command[1])
    else:
        aim -= (int)(command[1])

print(f'Horizontal: {horizontal}\tDepth: {depth}')
print(f'Product: {depth * horizontal}')