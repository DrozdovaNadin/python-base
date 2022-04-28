# Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.

# d = {
#     'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five', 'шесть': 'six', 'семь': 'seven', 'восемь': 'eight', 'девять': 'nine', 'десять': 'ten'
# }
# number_a = input('Введите число: ')
# number_a = number_a.lower()
# print(number_a)


def num_translate(number_a):
    d = {
        'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
        'eight': 'восемь', 'nine': 'девять', 'ten': 'деcять'
    }
    if number_a in d:
        # print(d[number_a])
        # return d.values(number_a)
        return (d[number_a])
    # if number_a is not None:
    #     return


number_a = input('Введите число: ')
number_a = number_a.lower()
# # print(number_a)
# num_translate(number_a)
print(num_translate(number_a))

