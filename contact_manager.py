import json
from colorama import init, Fore, Style

init(autoreset=True)

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if self.contacts:
            print(Fore.GREEN + "Contacts:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone}")
        else:
            print(Fore.YELLOW + "No contacts found.")

    def edit_contact(self, index, name, phone):
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1].name = name
            self.contacts[index - 1].phone = phone
            print(Fore.GREEN + "Contact updated successfully.")
        else:
            print(Fore.RED + "Invalid index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            print(Fore.GREEN + "Contact deleted successfully.")
        else:
            print(Fore.RED + "Invalid index.")

    def save_contacts(self, filename):
        with open(filename, "w") as file:
            json.dump([vars(contact) for contact in self.contacts], file)
        print(Fore.GREEN + "Contacts saved successfully.")

    def load_contacts(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.contacts = [Contact(**contact) for contact in data]
            print(Fore.GREEN + "Contacts loaded successfully.")
        except FileNotFoundError:
            print(Fore.RED + "File not found.")
        except json.decoder.JSONDecodeError:
            print(Fore.RED + "Invalid JSON format.")


if __name__ == "__main__":
    manager = ContactManager()

    manager.load_contacts("contacts.json")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Exit")
        print("-" * 20) 

        choice = input(Fore.CYAN + "Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            manager.add_contact(Contact(name, phone))
        elif choice == "2":
            manager.display_contacts()
        elif choice == "3":
            index = int(input("Enter index of contact to edit: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            manager.edit_contact(index, name, phone)
        elif choice == "4":
            index = int(input("Enter index of contact to delete: "))
            manager.delete_contact(index)
        elif choice == "5":
            manager.save_contacts("contacts.json")
        elif choice == "6":
            print(Fore.YELLOW + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")