# Search contact
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip().lower()
    matches = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]

    if not matches:
        print("No matches found.")
        return

    print("\n--- Search Results ---")
    for contact in matches:
        print(f"Name: {contact['name']} | Phone: {contact['phone']} | "
              f"Email: {contact['email']} | Address: {contact['address']}")