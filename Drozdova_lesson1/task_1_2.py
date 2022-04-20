# Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.

# Взять нечетные числа из интервала и Возвести их в куб

number = 1
n = 1000
a = 0
while number < n:
    if number % 2 != 0:
        number_1 = number**3
        res = 0
        while number_1 > 0:
            got = number_1 % 10
            res = res + got
            number_1 //= 10
        if res % 7 == 0:
            a = a + number
        # print(number, res)
        #     print(a)
        print(number,'**3 =', number ** 3, '[', res, ']', 'накоп сумма', a)
    number += 1





# print(number,'**3=',number**3, '[',res,']','накоп сумма', a)
# Найти сумму цифр куба
# res = 0
# number_1 = 1256
# while number_1 > 0:
#     got = number_1 % 10
#     res = res + got
#     number_1 //= 10
# print(res)


# Проверить делится ли на 7
# Добавить в накопительное

# number = 1
# while number >=1 and number <= 1000:
#     if number % 2 != 0:
#         number_kub = number**3
#         number += 1
#         res = 0
#         while number_kub > 0:
#             a=number_kub
#             got = a % 10
#             res = res + got
#             a //= 10
#         print(number_kub)
#         print(res)
#             else:
#             number += 1
#


