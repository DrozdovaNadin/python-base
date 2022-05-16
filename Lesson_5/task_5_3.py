# Есть два списка: tutors - имена учеников,
# groups - названия их классов. Необходимо ре-
# ализовать генератор или функцию-генератор,
# возвращающий кортежи

# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена', 'Ольга',
# ]
# groups = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '10Г'
# ]
# # groups = [
# #     '9А', '7В', '9Б', '9В', '8Б'
# # ]
#
# # Первый вариант решения
# def gen_people():
#     i = 0
#     j = 0
#     while i < len(tutors):
#         if i >= len(groups):
#             # s = (tutors[i], 'None')
#             # print(s)
#             yield (tutors[i], None)
#             i += 1
#             j += 1
#         else:
#             # s = (tutors[j], groups[i])
#             # print(s)
#             yield (tutors[j], groups[i])
#             i += 1
#             j += 1
# gen = gen_people()
# print(f"Тип объекта: {type(gen)}")
# for el in gen_people():
#     print(el)


    # Второй вариант
def generator_people(tutors, groups):
    for idx, el in enumerate(tutors):
        if idx < len(groups):
            yield (tutors[idx], groups[idx])
        else:
            yield (tutors[idx], None)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
#groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
groups = ['9А', '7В', '9Б', '9В']

gen_tutors = generator_people(tutors, groups)
print(f"Тип объекта: {type(gen_tutors)}")
for el in gen_tutors:
    print(el)
