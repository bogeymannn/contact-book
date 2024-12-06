from save_contacts import save_to_file

def remove_contact(contacts):
    name = input("Enter the name of the contact to remove: ").strip().lower()
    found = False

    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            save_to_file(contacts)  # save_contacts-এর বদলে save_to_file
            print(f"Contact '{name}' removed successfully!")
            found = True
            break

    if not found:
        print(f"No contact found with the name '{name}'.")
