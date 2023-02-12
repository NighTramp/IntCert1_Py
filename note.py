from datetime import date

attributes = {'id': '',
               'date': '',
               'title': '',
               'subject': ''}

class Note:
    
    guid = 0
    id = 0

    def __init__(self, title, subject):
        self.title = title
        self.subject = subject
        self.note_date = date.today()
        self.id = self.guid
        self.__class__.guid += 1
    
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_note_date(self):
        return self.note_date
    
    def __str__(self):
        return str(dict(zip(attributes, 
                        [self.get_id(), 
                        str(self.get_note_date()), 
                        self.get_title(), 
                        self.get_subject()])))