# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх заданных списков.

# from random import choice

# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
from random import choice

# Создаем функцию с треьуемыми аргументвми
def get_jokes(n,nouns, adverbs, adjectives):
    # пустой список
    d = []
    # цикл для прохождения неоходимого количества раз
    for i in range(n):
        bonus = choice(nouns)
        bonus1 = choice(adverbs)
        bonus2 = choice(adjectives)
    # print(bonus, bonus1, bonus2)
    #     складываем строку
        f = f'{bonus} {bonus1} {bonus2}'
        # добавляем в список
        d.append(f)
    i+=1
    # print(d)
    return d


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(5,nouns, adverbs, adjectives))


#
# def get_jokes(n,a = nouns, c = adverbs, l = adjectives):
#     d = []
#     print(a,c,l)
#     for i in range(n):
#         bonus = choice(nouns)
#         bonus1 = choice(adverbs)
#         bonus2 = choice(adjectives)
#         print(bonus, bonus1, bonus2)
#         f = f'{bonus} {bonus1} {bonus2}'
#         d.append(f)
#     i+=1
#     print(d)
#
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# get_jokes(5,nouns, adverbs, adjectives)
