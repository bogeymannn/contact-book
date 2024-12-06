# Add contact
from save_contacts import save_to_file

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone number: ").strip()
    address = input("Enter address: ").strip()

    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return

    if phone in [contact['phone'] for contact in contacts]:
        print("Error: Phone number already exists.")
        return

    contact = {
        'name': name,
        'email': email,
        'phone': phone,
        'address': address
    }
    contacts.append(contact)
    save_to_file(contacts)
    print(f"Contact for {name} added successfully!")