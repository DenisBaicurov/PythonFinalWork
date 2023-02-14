import Writefile
import ClassNote
from colorama import Fore, Style
def add(input):
    listOfNotes = Writefile.readFromFile()
    for note in listOfNotes:
        if ClassNote.Note.getId(input) == ClassNote.Note.getId(note):
                ClassNote.Note.setId(input)
    listOfNotes.append(input)
    Writefile.writeTofileList(listOfNotes, 'a')
    print(Fore.GREEN + "Заметка добавлена")
    print(Style.RESET_ALL)    
    
def showAllById():
    try:
        listOfNotes = Writefile.readFromFile()
        for note in listOfNotes:
            print('id: ' + ClassNote.Note.getId(note))
    except Exception:
        print (Fore.RED + '\nНет ни одной задачи\n')
        print(Style.RESET_ALL)  

def show():
    try:
        listOfNotes = Writefile.readFromFile()
        for note in listOfNotes:
            print(ClassNote.Note.forShow(note))
    except Exception:
        print (Fore.RED + '\nНет ни одной задачи\n')
        print(Style.RESET_ALL)  

def showByDate(input):
    isEmpty = True
    listOfNotes = Writefile.readFromFile()
    for note in listOfNotes:  
        if input in ClassNote.Note.getDate(note) :
            print(ClassNote.Note.forShow(note))
            isEmpty =False
    if isEmpty == True:
        print(Fore.RED + "Задач не найдено")
        print(Style.RESET_ALL)  


def showById(input):
    isEmpty = True
    listOfNotes = Writefile.readFromFile()
    for note in listOfNotes:  
       if input == ClassNote.Note.getId(note):
            print(ClassNote.Note.forShow(note))
            isEmpty = False
    if isEmpty == True:
        print(Fore.RED + "Задач не найдено")
        print(Style.RESET_ALL)  


def delete(input):
    isDeleted = False
    listOfNotes = Writefile.readFromFile()
    for note in listOfNotes:  
        if input == ClassNote.Note.getId(note) :
            isDeleted = True
            listOfNotes.remove(note)
            print(Fore.GREEN + "Заметка удалена")
            print(Style.RESET_ALL)  
    Writefile.writeTofileList(listOfNotes, 'a')
    if isDeleted == False :
        print(Fore.RED + 'Такой заметки нет. Возможно вы ввели неверный id')
        print(Style.RESET_ALL)  


def edit(input, newTitle, newBody):
    listOfNotes = Writefile.readFromFile()
    for note in listOfNotes:  
        if input == ClassNote.Note.getId(note) :
            ClassNote.Note.setTitle(note,newTitle)
            ClassNote.Note.setBody(note, newBody)
            ClassNote.Note.setDate(note)
            print(Fore.GREEN + 'Заметка изменена')
            print(Style.RESET_ALL)  
    Writefile.writeTofileList(listOfNotes, 'a')
    