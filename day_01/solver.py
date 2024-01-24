import re
import sys

digitDictionary = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}


def readFile():
    # Read file
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    return lines


def toDigits(value):
    """
    >>> toDigits('one')
    '1'
    >>> toDigits('two')
    '2'
    >>> toDigits('three')
    '3'
    >>> toDigits('four')
    '4'
    """
    if value in digitDictionary.keys():
        return digitDictionary[value]
    else:
        return value


def solve(line):
    """
    >>> solve('1-3 a: abcde')
    13
    >>> solve('1abc2')
    12
    >>> solve('two1nine')
    29
    >>> solve('eighthree')
    83
    """
    regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine|ten))'
    digits = re.findall(regex, line)
    first = toDigits(digits[0])
    last = toDigits(digits[-1])
    # Solve
    return int(first + last)


def main():
    lines = readFile()
    total = 0
    for line in lines:
        total += solve(line)

    print(total)


if __name__ == '__main__':
    args = sys.argv
    if 'test' in args:
        import doctest
        doctest.testmod()
    else:
        main()
