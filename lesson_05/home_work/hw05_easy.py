# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os

#мой вариант
"""
for i in range (1,10):
    new_dir = ('dir_{}'.format(i))
    os.mkdir(new_dir)

for i in range (1,10):
    dir_del = ('dir_{}'.format(i))
    os.rmdir(dir_del)
"""

# из семинара
"""
def make_dirs ():
    for i in range (1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            os.mkdir (dir_path)
            print ('Создана директория: {dir_path}')
        except FileExistsError:
            print ('Папка уже создана: {dir_path}')

def remove_dirs():
    for i in range (1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            os.rmdir (dir_path)
            print ('Удалена директория: {dir_path}')
        except FileExistsError:
            print ('Такой директории нет: {dir_path}')
make_dirs ()
remove_dirs ()
"""

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

"""
#мой вариант
print (os.listdir('./'))
"""

# из семинара

def list_current_dir ():
    elems = os.listdir(os.getcwd())
    for el in elems:
        if os.path.isdir(el):
            print (el)

list_current_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import sys

#мой вариант
"""
print (__file__)
shutil.copy(r'hw05_easy.py', r'hw05_easy_copy.py')
"""

# из семинара
"""
def copy_dir ():
    shutil.copy(sys.argv[0], os.path.join(os.getcwd(), 'copy.py'))
copy_dir()
"""