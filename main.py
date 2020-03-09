#1
class Contact():
    def __init__(self, first_name, second_name, telephone_number, *args, favorite_contact=False, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.telephone_number = int(telephone_number)
        self.favorite_contact = favorite_contact
        self.list_extra = args
        self.dict_extra = kwargs

    def __str__(self):
        s1 = (f'Имя: {self.first_name}\n\
Фамилия: {self.second_name}\n\
Телефон: {self.telephone_number}\n\
Дополнительная информация:\n\t')
        s2 = '\n\t'.join(list([x + ': ' + str(self.dict_extra[x]) for x in self.dict_extra])) + '\n\t'
        s3 = '\n\t'.join(list([str(x) for x in self.list_extra]))
        if self.favorite_contact == True:
            return s1 + 'Любимый контакт' + s2 + s3
        else:
            return s1 + s2 + s3

class PhoneBook(Contact):

    def __init__(self, name):
        self.book_name = name
        self.all = []
        self.numbers = []

    def new_contact(self, first_name, second_name, telephone_number, *args, favorite_contact = False, **kwargs):
        new = Contact(first_name, second_name, telephone_number, *args, favorite_contact, **kwargs)
        if new.telephone_number in self.numbers:
            print(f'There is a contact with number {new.telephone_number} already!')
            del new
        else:
            self.numbers.append(new.telephone_number)
            self.all.append(new)

    def view_all(self):
        for contact in self.all:
            print(Contact.__str__(contact))

    def delete_contact(self, number):
        for c in self.all:
            print(c.telephone_number)
            if c.telephone_number == number:
                print(f'{c.first_name} just deleted!')
                self.all.remove(c)
                self.numbers.remove(number)
            else:
                print('There is no such contact!')

    def search(self, fname, sname):
        for contact in self.all:
            if contact.first_name == fname and contact.second_name == sname:
                print(contact)
            else:
                print('There is no such contact!')
