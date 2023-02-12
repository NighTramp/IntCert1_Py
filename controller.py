from note import Note
from dataadapter import DataAdapter

class Controller:

    attributes = {'id': '',
               'date': '',
               'title': '',
               'subject': ''}

    notes = []

    def __init__(self):
        self.view()

    def view(self):
        print('Command List:\n'
          '   add - add note,\n'
          '   mod - modify note,\n'
          '   del - delete note,\n'
          '   filter - filter note by date and view result,\n'
          '   search - search note by id and view result,\n'
          '   readall - view all notes,\n'
          '   import - import all notes from *.csv file,\n'
          '   export - export all notes to *.csv file,\n'
          '   exit')
        while True:
            choose = input('\nPlease enter the command: ')

            match(choose):
                case 'add':
                    obj = Note(input('Please enter the title: '), 
                               input('Please enter the message: '))
                    self.notes.append(obj)

                case 'mod':
                    try:
                        id = int(input('Please enter the id: '))
                        flag = False
                        for obj in self.notes:
                            if obj.get_id() == id:
                                flag = True
                                txt = input('Please enter the title: ')
                                if txt != '':
                                    obj.title = txt
                                txt = input('Please enter the subject: ')
                                if txt != '':
                                    obj.subject = txt
                        if flag == False:
                            print('Note not found')
                    except ValueError:
                         print('Value error.')

                case 'del':
                    try:
                        id = int(input('Please enter the id: '))
                        flag = False
                        for obj in self.notes:
                            if obj.get_id() == id:
                                flag = True
                                self.notes.remove(obj)
                        if flag == False:
                            print('Note not found')
                    except ValueError:
                         print('Value error.')

                case 'search':
                    try:
                        id = int(input('Please enter the id: '))
                        flag = False
                        for obj in self.notes:
                            if obj.get_id() == id:
                                flag = True
                                print(obj)
                        if flag == False:
                            print('Note not found')
                    except ValueError:
                         print('Value error.')
                
                case 'filter':
                    try:
                        date = input('Please enter the date: ')
                        flag = False
                        for obj in self.notes:
                            if obj.get_note_date() == date:
                                flag = True
                                print(obj)
                        if flag == False:
                            print('Note not found')
                    except ValueError:
                         print('Value error.')

                case 'readall':
                    for obj in self.notes:
                        print(obj)

                case 'export':
                    DataAdapter.data_export(input('Please enter the filename: '), self.notes)

                case 'import':
                    DataAdapter.data_import(input('Please enter the filename: '), self.notes)

                case 'exit':
                    break

                case _:
                    print('Unnown command. Please, try again.')

