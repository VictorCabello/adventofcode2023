import re
import sys


def readFile():
    # Read file
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    return lines


def findRed(line):
    """
    >>> findRed('3 blue, 4 red')
    {'blue': 3, 'red': 4}
    """
    myRegex = r'(\d+) (\w+)'
    m = re.findall(myRegex, line)
    m = [(t[1], int(t[0])) for t in m]
    if m:
        return dict(m)
    else:
        return None


def getSetInfo(line):
    """
    >>> getSetInfo('3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]
    """
    sets = line.split(';')
    setList = []
    for set in sets:
        setInfo = findRed(set)
        if setInfo:
            setList.append(setInfo)

    return setList


def getGameInfo(line):
    """
    >>> getGameInfo('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    {'id': '1', 'setList': [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]}
    """
    myRegex = r'^Game (\d+): (.*)$'
    m = re.search(myRegex, line)
    if m:
        id = m.group(1)
        rawSetInfo = m.group(2)
        setList = getSetInfo(rawSetInfo)
        return {
            'id': int(id),
            'setList': setList
        }
    else:
        return None


def isColorValid(colorCount, maxAllowed):
    """
    >>> isColorValid(3, 14)
    True
    """
    return colorCount <= maxAllowed


def isGameValid(game):
    """
    >>> isGameValid({'id': '1', 'setList': [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]})
    True
    """
    setList = game['setList']
    redAllowed = 12
    blueAllowed = 14
    greenAllowed = 13
    isValid = True
    for mySet in setList:
        if 'red' in mySet.keys():
            isValid = isValid and isColorValid(mySet['red'], redAllowed)
        if 'blue' in mySet.keys():
            isValid = isValid and isColorValid(mySet['blue'], blueAllowed)
        if 'green' in mySet.keys():
            isValid = isValid and isColorValid(mySet['green'], greenAllowed)

    return isValid


def main():
    lines = readFile()
    total = 0
    for line in lines:
        line = line.strip()
        if line:
            gameInfo = getGameInfo(line)
            if gameInfo:
                if isGameValid(gameInfo):
                    total += gameInfo['id']
    print(total)


if __name__ == "__main__":
    args = sys.argv
    if 'test' in args:
        import doctest
        doctest.testmod()
    else:
        main()
