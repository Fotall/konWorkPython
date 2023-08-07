import datetime
import json


def new_file():
    name = input('Введите название заметки: ')
    with open(name + ".json", "w", encoding='utf-8') as file:
        text_file = input('Введите текст заметки: ')
        now = datetime.datetime.now()
        some_list = ['Заметка', name, ' создана ', now]
        file.writelines(text_file)
        print(*some_list)

    # file = open(name + ".txt", "a+", encoding='utf-8')
    # now = datetime.datetime.now()
    # file.write(now)
    # file.close()

def editor_file():
    name = input('Введите название заметки, которую хотите изменить: ')
    file = open(name + ".json", "a", encoding='utf-8')
    text_file = input('Введите текст заметки: ')
    file.write(text_file,)
    file.close()

def read_file():
    name = input('Введите название заметки, которую хотите посмотреть: ')
    with open(name + ".json", "r", encoding='utf-8') as file:
        text = file.read()
        print(text)

lch = int(input('Укажите цифру, что вы хотите: 1 - ввести данные в заметку; 2 - изменить заметку,  3 - посмотреть заметку.'))
if lch == 1:
    new_file()
elif lch == 2:
    editor_file()
elif lch == 3:
    read_file()
else:
    print('не верно указана цифра')