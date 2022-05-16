# Задан список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов
# список с сохранением порядка их следования в исходном списке

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

# a = [el for el in src if src.count(el) == 1]
# print(a)

unique_brands = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique_brands.add(el)
    else:
        unique_brands.discard(el)
    tmp.add(el)
print(unique_brands)
# print(tmp)
unique_l = [el for el in src if el in unique_brands]
print(unique_l)