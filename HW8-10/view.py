import text
from model import Contact, PhoneBook

def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')

    while True:
        choice = input(text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)

def print_message(msg):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n' )

def show_book(book: PhoneBook, msg: str, print_items: dict[int, Contact] = None):

    if print_items is None:
        print_items = book.phone_book

    if print_items:        
        print('\n' + '*' * (book.max_len("name") + book.max_len("phone") + book.max_len("comment") + 5))
        for i, contact in print_items.items():
            print(f'{i:>3}. {contact.name:<{book.max_len("name") + 5}}'
                  f'{contact.phone:<{book.max_len("phone") + 5}}'
                  f' {contact.comment:<{book.max_len("comment")}}') 
        print('*' * (book.max_len("name") + book.max_len("phone") + book.max_len("comment") + 5) + '\n' )
    else:
        print_message(msg)

def input_contact(msg: str) -> list[str]:
    contact = []
    for input_text in msg:
        contact.append(input(input_text))
    return contact

def input_request(msg:str) -> str:
    return input(msg)



