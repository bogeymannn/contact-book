## View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']} | Phone: {contact['phone']} | 
               f"Email: {contact['email']} | Address: {contact['address']}")