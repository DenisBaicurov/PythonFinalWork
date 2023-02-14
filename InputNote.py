import ClassNote

from colorama import Fore, Style 
import keyboard

def createNote():
    note = editNote()   
    return ClassNote.Note(title = note[0], body = note[1])


def editNote():
    title = ''
    body = ''
    while len(title)<=4:
        print('<Заголовок должен быть больше 4 символов>\n')
        title = input('Введите ЗАГОЛОВОК заметки: ')
    while len(body)<=4:
        print('<Заметка должен быть больше 4 символов>\n')
        body = input('\rВведите ОПИСАНИЕ заметки: ')
    return (title, body)


def menu():
    print('\n' * 50)
    print(Fore.CYAN + 'Добро пожаловать в программу "Заметки"')
    print(Style.RESET_ALL) 
    print(Fore.MAGENTA + "\n1 - для вывода всех заметок\n2 - для добавления заметки\n3 - для удаления заметки\n4 - для редактирования заметки\n5 - для выборки по дате\n6 - показать элемент по id\n7 - для выхода\n")
    print(Style.RESET_ALL)  

def continueWork():
    print('Нажмите пробел для продолжения...')
    keyboard.wait('space')
    