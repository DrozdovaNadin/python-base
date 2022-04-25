list = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12]
for ls in range(len(list)):
    # print(list[ls])
    a = int(list[ls]//1)
    b = round(list[ls] % a,3)
    x = str(b)
    if len(x) < 4:
        n = x[2:] + '0'
    elif len(x) >= 4:
            n = x[2:]
    else:
        n = '00'
    print(a,'руб', n,'коп')

print(id(list))
list.sort()
print(list)
print(id(list))

list1 = sorted(list, reverse=True)
print(list1)
print(id(list1))

max_list = list1[:5]
# print(max_list)
print('Пять самых дорогих товаров:')
for el in max_list:
    print(el)