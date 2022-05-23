import sys
# print(sys.argv)
a = sys.argv[1]
# print(type(a))
with open('bakery.csv', 'a+', encoding= 'Utf-8') as f:
    if len(sys.argv) > 2:
        # print(a)
        print('Введите одну сумму')
    elif a.isdigit() == False:
        print("Введите числовое значение")
    else:
        f.write(a + '\n')