from os import  mkdir, makedirs
from os.path import join

a = ['settings', 'mainapp', 'adminapp', 'authapp']
for lis in a:
    p1 = join('.', "my_project", lis)
    makedirs(p1, exist_ok=True)