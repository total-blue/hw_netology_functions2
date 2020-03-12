#1
class Contact():
    def __init__(self, first_name, second_name, telephone_number, favorite_contact=False, *args, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.telephone_number = int(telephone_number)
        self.favorite_contact = favorite_contact
        self.list_extra = list(args)
        self.dict_extra = kwargs
        if not type(self.favorite_contact) == bool:
            unit = self.favorite_contact
            self.favorite_contact = False
            self.list_extra.insert(0, unit)


    def __str__(self):
        fav = 'да' if self.favorite_contact else 'нет'
        s1 = (f'Имя: {self.first_name}\n\
Фамилия: {self.second_name}\n\
Телефон: {self.telephone_number}\n\
В избранных: {fav}\n\
Дополнительная информация:\n\t')
        if self.dict_extra:
            s2 = '\n\t'.join(list([x + ': ' + str(self.dict_extra[x]) for x in self.dict_extra])) + '\n\t'
        else:
            s2 = None
        if self.list_extra:
            s3 = '\n\t'.join(list([str(x) for x in self.list_extra]))
        else:
            s3 = None
        if s2 and s3:
            return s1 + s2 + s3
        elif not s2 and s3:
            print(s3)
            return s1 + s3
        elif s2 and not s3:
            return s1 + s3
        else:
            return s1[:-len('Дополнительная информация:\n\t')]

class PhoneBook(Contact):

    def __init__(self, name):
        self.book_name = name
        self.all = []
        self.numbers = []

    def new_contact(self, first_name, second_name, telephone_number, favorite_contact=False, *args, **kwargs):
        new = Contact(first_name, second_name, telephone_number, favorite_contact, *args, **kwargs)
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
        number = int(number)
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

    def show_all_favorite(self):
        for contact in self.all:
            if contact.favorite_contact: print(contact)

#2
def adv_print(*args, **kwargs):
    args = list(args)
    kwargs = kwargs

    try:
        text = args.pop(0)
    except Exception:
        raise SyntaxError('Missing 1 positional argument')
    fields = ['start', 'max_line', 'in_file']
    args_dict = dict(zip(fields, args))

    for key in kwargs:
        if key in args_dict:
            raise SyntaxError('To many arguments')
        elif not key in fields:
            raise SyntaxError('Wrong keyword argument')
    args_dict.update(kwargs)

    if 'start' in args_dict.keys():
        len_start = len(str(args_dict['start']))
        start = args_dict['start']
    else:
        len_start = 0

    if 'max_line' in args_dict.keys():
        try:
            args_dict['max_line'] = int(args_dict['max_line'])
        except Exception:
            raise SyntaxError('Wrong value for max_line')
        if len_start >= args_dict['max_line']:
            raise SyntaxError('Too long start for this max_line')
        string_len = args_dict['max_line'] - len_start
        splitted_text = []
        for i in range(string_len, len(text)):
            if i % string_len == 0:
                splitted_text.append(text[i-string_len:i])
                tail = i
        splitted_text.append(text[tail:])
        splitted_text = [f'{start}{x}' for x in splitted_text]
        res = '\n'.join(splitted_text)
    else:
        res = f'{start}{text}'

    print(res)

    if 'in_file' in args_dict.keys():
        file_name = str(args_dict['in_file']) + '.txt'
        f = open(file_name, 'w')
        f.write(res)
        f.close()
