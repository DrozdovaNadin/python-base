# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield. Полностью истощить генератор.
def nums_generator(n):
    for num in range(1, n + 1, 2):
        yield num
nums_gen = nums_generator(11)
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))