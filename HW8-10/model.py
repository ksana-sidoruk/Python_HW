class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment
    
    def __str__(self):
        return self.name

class PhoneBook:
    def __init__ (self, path): 
        self.path = path 
        self.phone_book: dict[int, Contact] = {}


    def open_file(self):
        with open(self.path, 'r', encoding = 'UTF-8') as file:
            data = file.readlines()
            for i, contact in enumerate(data, 1):
                contact = contact.strip().split(':')
                self.phone_book[i] = Contact(*contact)
        
    def save_file(self):
        data = []
        for contact in self.phone_book.values():
            contact = ':'.join([contact.name, contact.phone, contact.comment])
            data.append(contact)
        data = '\n'.join(data)
        with open(self.path, 'w', encoding = 'UTF-8') as file:
            file.writelines(data)

    def add_contact(self, new_contact: list[str]):
        c_id = max(self.phone_book) + 1
        self.phone_book[c_id] = Contact(*new_contact)

    def find_contact(self, word: str) -> dict[int, Contact]:
        result = {}
        for c_id, contact in self.phone_book.items():
            if word.lower() in contact.name.lower():
                result[c_id] = contact
                continue
            if word.lower() in contact.phone.lower():
                result[c_id] = contact
                continue    
            if word.lower() in contact.comment.lower():
                result[c_id] = contact
                continue
        return result

    def edit_contact(self, c_id: int, new_contact: list[str]):
        current_contact = self.phone_book.get(c_id)
        if new_contact[0]:
            current_contact.name = new_contact[0]
        if new_contact[1]:
            current_contact.phone = new_contact[1]
        if new_contact[2]:
            current_contact.comment = new_contact[2]
        return current_contact

    def delete_contact(self, c_id: int) -> str:
        return self.phone_book.pop(c_id).name

    def max_len(self, option: str):
        result = []
        for contact in self.phone_book.values():
            if option == 'name':
                item = contact.name
            elif option == 'phone':
                item = contact.phone
            else:
                item = contact.comment
            result.append(item)
        return len(max(result, key = len))