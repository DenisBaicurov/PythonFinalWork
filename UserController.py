import Examnationlist
import WorkofNote
import InputNote
from colorama import Fore, Style
def start():
    userInput ='0'
    while userInput != '7':
        InputNote.menu() 
        userInput =input('Введите номер задачи: ').strip()
        print("\n")
        if userInput == '1':
           WorkofNote.show()
           InputNote.continueWork()
        if userInput == '2':
            note =InputNote.createNote()
            WorkofNote.add(note)
            InputNote.continueWork()
        if userInput == '3':
            WorkofNote.show()
            print("\n")
            WorkofNote.delete(input("Введите id заметки: "))
            InputNote.continueWork()
        if userInput == '4':
            WorkofNote.show()
            print("\n")
            userInput = input("Введите id заметки: ")
            if Examnationlist.checkInList(userInput):
                editNote = InputNote.editNote()
                WorkofNote.edit(userInput, editNote[0], editNote[1])
            else:
                print(Fore.RED + 'Нет такой заметки. Возможно вы ввели неверный id')
                print(Style.RESET_ALL)  
            InputNote.continueWork()        
        if userInput == '5':
            WorkofNote.showByDate(input('Введите дату в формате день.месяц.год: '))
            print('\n')
            InputNote.continueWork()
        if userInput == '6':
            WorkofNote.showAllById()
            print("\n")
            WorkofNote.showById(input("Введите id заметки: "))
            InputNote.continueWork()
        if userInput == '7':
            print("Спасибо, что выбрали это приложение. До свидания!")
            break