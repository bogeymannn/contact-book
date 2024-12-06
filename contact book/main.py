
from remove_contacts import remove_contact
from save_contacts import load_from_file,save_to_file
from view_contact import view_contacts
from search_contacts import search_contact
from contact_add import add_contact
# Main program
def main():
    contacts = load_from_file()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            remove_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '0':
            print("Well Done")
            break
        else:
            print("Invalid choice. Please try again.")

