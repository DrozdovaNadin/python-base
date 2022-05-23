from sys import argv
import sys
# print(sys.argv[1])
# print(type(sys.argv[1]))

with open('bakery.csv', 'r', encoding='Utf-8') as f:
    if len(sys.argv) == 1:
        content = f.read()
        print(content)
    elif len(sys.argv) == 2:
        if sys.argv[1].isdigit() == True:
            start = int(sys.argv[1])
            lines = f.readlines()
            d = (lines[start-1:])
            for line in d:
                print("".join(line).strip())
        else:
            print("Введите число")
    elif len(sys.argv) == 3:
        if sys.argv[2].isdigit() == True:
            if sys.argv[2] > sys.argv[1]:
                start = int(sys.argv[1])
                finish = int(sys.argv[2])
                lines = f.readlines()
                d = (lines[start - 1:finish])
                for line in d:
                    print("".join(line).strip())
            else:
                print("Неправильный диапазон")
        else:
            print("Введите число")
    elif len(sys.argv) > 3:
        print("Введите правильный диапазон")





