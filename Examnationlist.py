import ClassNote
import Writefile
def checkInList(input):
    listOfNotes = Writefile.readFromFile()
    for note in listOfNotes:  
        if input == ClassNote.Note.getId(note):
            return True