
from os import  walk, makedirs, getcwd
from os.path import join
from shutil import copytree, copy2

# вывести текущую директорию
# print("Текущая деректория:", os.getcwd())
# p1 = join('.', "my_project", 'templates')
# makedirs(p1, exist_ok=True)

p2 = join('.', "my_project")
for name, dirs, files in walk(p2):
    for names in dirs:
        # print(os.path.join(name, names))
        if names == 'templates':
           p = os.path.join(name, names)
           p1 = join('.', "my_project", 'templates')
           copytree(p, p1,copy_function=copy2, dirs_exist_ok=True )
#

