import os
lines = []

with open(os.path.join(os.path.dirname(__file__), "input2.txt")) as f:
    for line in f:
        lines.append(line.strip())

charDict = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

pointDict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def processLine(line):
    pendingTags = []
    for char in line:
        if char in charDict:
            # If this is not a closing tag
            pendingTags.append(char)
        else:
            # This is a closing tag
            correctCloseTag = charDict[pendingTags.pop()]
            if char != correctCloseTag:
                pointValue = pointDict[char]
                print(
                    f'Line: {line}\tScore: {pointValue}\tIllegal Character: {char}')
                return pointValue
    return 0


incompleteLines = []

score = 0
for line in lines:
    newPoints = processLine(line)
    if newPoints == 0:
        incompleteLines.append(line)
    score += newPoints

print(f'Score: {score}')

# Part 2
part2ScoreDict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def fixIncompleteLine(line):
    pendingTags = []
    for char in line:
        if char in charDict:
            # If this is not a closing tag
            pendingTags.append(char)
        else:
            # This is a closing tag
            pendingTags.pop()

    pendingTags.reverse()
    print(f'line: {line}\ttagsToClose: {pendingTags}')
    returnVal = 0
    for openingTag in pendingTags:
        returnVal *= 5
        returnVal += part2ScoreDict[charDict[openingTag]]

    return returnVal


part2Scores = []
for line in incompleteLines:
    part2Scores.append(fixIncompleteLine(line))
part2Scores.sort()

print(f'Part 2 Scores: {part2Scores}')
print(f'Middle Score: {part2Scores[(int)(len(part2Scores) / 2)]}')
