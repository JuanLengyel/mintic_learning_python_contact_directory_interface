class Contact:

    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email

    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone

    def get_email(self):
        return self._email
    
    def set_name(self, name):
        self._name = name

    def set_phone(self, phone):
        self._phone = phone

    def set_email(self, email):
        self._email = email