from note import Note

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
                    self.notes.append(dict(zip(self.attributes, 
                                               [obj.get_id(),
                                                str(obj.get_note_date()),
                                                obj.get_title(),
                                                obj.get_subject()])))
                case 'readall':
                    for obj in self.notes:
                        print(obj)
                case 'exit':
                    break
                case _:
                    print('Unnown command. Please, try again.')

