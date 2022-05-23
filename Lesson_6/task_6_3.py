# Есть два файла: в одном хранятся ФИО
# пользователей сайта, а в другом — данные об
# их хобби. Загрузить данные из обоих файлов
# и сформировать словарь: ключи — ФИО, зна-
# чения — данные о хобби. Сохранить словарь в
# текстовый файл. Проверить сохранённые дан-
# ные.


with open('task_3_users.csv', 'w+', encoding='utf-8') as file_1:
    file_1.write('Иванов,Иван,Иванович\n'
    'Петров,Петр,Петрович\n')
    # 'Сидоров,Сидор,Сидорович\n'
    # 'Кузьмин,Олег,Сидорович')


with open('task_3_hobby.csv', 'w+', encoding='utf-8') as file_2:
    file_2.write('скалолазание;охота.\n'
    'горные лыжи.\n'
    'вышивание крестиком; бои без правил')


with open('task_3_users.csv', 'r', encoding='utf-8') as file_1:
    content = file_1.read()
    list1 = content.splitlines()
    print(list1)

with open('task_3_hobby.csv', 'r', encoding='utf-8') as file_2:
    content = file_2.read()
    list2 = content.splitlines()
    print(list2)



dic = {}
length = len(list2)
for idx, man in enumerate(list1):
    man = man.replace(',', ' ')
    man = '{:.1}{:.1}{:.1}'.format(*man.split())
    if idx < length:
        dic[man] = list2[idx]
    elif idx > length:
        exit(1)
    else:
        dic[man] = None
    # dic[man] = list2[idx]
print(dic)

with open('task_3_rezult.txt', 'w', encoding='utf-8') as f:
    f.write(str(dic))
