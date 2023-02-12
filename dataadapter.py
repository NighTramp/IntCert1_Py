import csv
from note import Note

class DataAdapter:

    def data_export(filename, list):
        with open(filename, 'w', newline='') as f:
            fieldnames = ['id', 'date', 'title', 'subject']
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            for row in list:
                writer.writerow(row.get_dict())
        return True

    def data_import(filename, list):
        list.clear()
        Note.guid = 0
        with open(filename, newline='') as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                item = Note(row['title'],row['subject'])
                item.note_date = row['date']
                list.append(item)
        return list
