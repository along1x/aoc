import os

numwords = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

total = 0
with open('2023/inputs/1.txt', 'r') as fin:
    line = fin.readline()
    while line:
        numchars = []
        for i in range(len(line)):
            if line[i].isnumeric():
                numchars.append(line[i])
            else:
                for word, num in numwords.items():
                    if line[i:].startswith(word):
                        numchars.append(num)
                        break

        value = int(numchars[0] + numchars[-1])
        print(value)
        total += value
        line = fin.readline()

print("sum:", total)