import csv

def load_from_file(filename="contacts.csv"):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)  # Return a list of dictionaries
    except FileNotFoundError:
        return []

def save_to_file(contacts, filename="contacts.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['name', 'email', 'phone', 'address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
    print("Contacts saved to file.")

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone number: ").strip()
    address = input("Enter address: ").strip()
    if not phone.isdigit():
        print("Error: Phone number must be an integer.")
        return
    if phone in [contact['phone'] for contact in contacts]:
        print("Error: Phone number already exists.")
        return
    contacts.append({'name': name, 'email': email, 'phone': phone, 'address': address})
    print(f"Contact for {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to remove: ").strip()
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact removed successfully!")
            return
    print("Contact not found.")

def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip()
    results = [contact for contact in contacts if query in contact['name'] or query in contact['phone']]
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

def main():
    contacts = load_from_file()
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Save and Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            remove_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            save_to_file(contacts)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
