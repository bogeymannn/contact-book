from contact_add import add_contacts
from save_to_file import load_from_file
from view_contacts import view_contacts
from remove_contact import remove_contact
from search_contact import search_contact







contacts = load_from_file()
while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("0.  Exit")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        add_contacts(contacts)
    elif choice == '2':
        view_contacts(contacts)
    elif choice == '3':
        remove_contact(contacts)
    elif choice == '4':
        search_contact(contacts)
    elif choice == '0':
        print("good bye!")
        break
    else:
        print("Invalid choice. Please try again.")


