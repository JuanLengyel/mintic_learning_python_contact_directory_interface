import csv
from contact import Contact

class ContactBook:

    def __init__(self):
        self._contacts = []
        self._load()

    def add(self, name, phone, email):
        self._contacts.append(Contact(name, phone, email))
        self._save()

    def remove(self, name):
        try:
            self._contacts.remove(self._search(name))
        except ValueError:
            self._not_found(name)
        finally:
            self._save()
    
    def searchAndPrint(self, name):
        try:
            self._print_contact(self._search(name))
        except AttributeError:
            self._not_found(name)

    def update(self, name):
        try:
            foundContact = self._search(name)

            foundContact.set_name(str(raw_input("Input updated name: ")))
            foundContact.set_phone(str(raw_input("Input updated phone: ")))
            foundContact.set_email(str(raw_input("Input updated email: ")))
        except AttributeError:
            self._not_found(name)
        finally:
            self._save()

    def show_contacts(self):
        map(lambda contact: self._print_contact(contact), self._contacts)

    def _print_contact(self, contact):
        print("***-----------------------****")
        print("Name: {}".format(contact.get_name()))
        print("Phone: {}".format(contact.get_phone()))
        print("Email: {}".format(contact.get_email()))
        print("***-----------------------****")
    
    def _not_found(self, name):
        print("The contact with name {} was not found".format(name))

    def _search(self, name):
        for contact in self._contacts:
            if (contact.get_name().lower() == name.lower()):
                return contact
                break
        else:
            return AttributeError

    def _save(self):
        with open("contacts.csv", "w") as f:
            f.write("name,phone,email\n")
            f.write(str.join("\n", map(lambda contact: "{},{},{}".format(contact.get_name(), contact.get_phone(), contact.get_email()), self._contacts)))
            f.close
    
    def _load(self):
        with open('contacts.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx < 1:
                    continue
                self._contacts.append(Contact(row[0], row[1], row[2]))