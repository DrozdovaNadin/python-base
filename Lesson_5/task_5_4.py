# Задан список чисел. Необходимо создать список, содержащий те его элементы, значения которых больше предыдущего.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

# answer = []
# for i in range(len(src)-1):
#     if src[i] < src[i+1]:
#         answer.append(src[i+1])
#
# print(answer)

list1 = [src[idx] for idx in range(1, len(src)) if src[idx] > src[idx-1]]
print(list1)
