# Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield, полностью истощить генератор.

def iterator_without_yield(n):
    nums_gc = (el for el in range(n) if el %2 != 0)
    return nums_gc

s = iterator_without_yield(11)

print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))