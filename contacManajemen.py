class Contact():
    def __init__(self, name, phone, email) :
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f"Nama: {self.name}, Telepon: {self.phone}, Email: {self.email}"


class ContactManager():
    def __init__(self, name) :
        self.name = name
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def display_contacts(self):
        print(f"Selamat Datang di Aplikasi {self.name}")
        print(f"Daftar Kontak")
        for id, contact in enumerate(self.contacts, start=1):
            print(f"{id}. {contact}")

def main():
    app = ContactManager("Manajemen Kontak")

    kontak1 = Contact("Jhon Doe",1234567890,"jhon@example.com")
    kontak2 = Contact("Jane Smith",9876543210,"jane@example.com")

    app.add_contact(kontak1)
    app.add_contact(kontak2)
    app.display_contacts()

    print(f"Hapus kontak {kontak1.name} dari daftar")
    app.remove_contact(kontak1)
    app.display_contacts()



if __name__ == "__main__":
    main()


    

      