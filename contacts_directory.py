from contact_book import ContactBook

def run():
    while True:
        command = str(raw_input('''
        What would you like to do?

        [a]dd a new contact
        [u]pdate a contact
        [s]earch a contact
        [r]emove a contact
        [l]ist all your contacts
        [e]xit
        '''))

        if (command == 'a'):
            name = str(raw_input("Input the contacts name: "))
            phone = str(raw_input("Input the contacts phone: "))
            email = str(raw_input("Input the contacts email: "))
            contact_book.add(name, phone, email)
        elif (command == 'u'):
            name = str(raw_input("Input name contact to update: "))
            contact_book.update(name)
        elif (command == 's'):
            name = str(raw_input("Input name contact to show: "))
            contact_book.searchAndPrint(name)
        elif (command == 'r'):
            name = str(raw_input("Input name contact to delete: "))
            contact_book.remove(name)
        elif (command == 'l'):
            contact_book.show_contacts()
        elif (command == 'e'):
            print("Goodbye")
            return
        else:
            print("I couldn't understand that commend, try again")

if __name__ == "__main__":
    contact_book = ContactBook()
    run()