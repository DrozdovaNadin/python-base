# Дан список строк. Выполнить обработку списка (смотри текст задания) и сформировать на его основе строку

list1 = ['в', '5', 'часов', '-17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов', '3', 'градуса', '-8', 'процентов']
new_list = []
for id, ren in enumerate(list1):
    if ren[0] == "+" or ren[0] == "-" and ren[1:].isdigit() or ren.isdigit():
        if len(ren) <= 2 and len(ren) > 1 :
            ren = (f'{ren[0]}0{ren[1:]}')
        elif len(ren) == 1:
            ren = (f'0{ren[0:]}')
        new_list.append('"')
        new_list.append(ren)
        new_list.append('"')
    else:
        new_list.append(ren)
print(new_list)



list1 = ''
for index in range(len(new_list)-1):
    x1 = new_list[index]
    x2 = new_list[index+1]
    if x1 == '"' and x2.isdigit():
        x1 = x1 + x2
        list1 = list1 + x1
        # list1.append(x1)
    elif x1[0] == '-' or x1[0] == '+'and x1[1:].isdigit():
        x1 = new_list[index-1] + x1 + new_list[index+1] + " "
        list1 = list1 + x1
    elif x1.isdigit():
        x1 = new_list[index+1] + " "
        list1 = list1 + x1
    elif x1 == '"':
        x1.replace('"', " ")
    else:
        list1 = list1 + x1 + ' '
# print(list1)
if new_list[-1].isdigit() == False:
    list1 = list1 + new_list[-1]
print(list1)
















# list2 = []
# for id, ren in enumerate(list2):
#     if ren.isdigit():
#         list2.insert(id, '"')
#         list2.append(ren)
#         list2.append('"')
#     if ren[0] == "+" or ren[0] == "-":
#         new_list.insert(id, '"')
#         list2.append(ren)
#         list2.append('"')
#     else:
#         list2.append(ren)
# print(list2)