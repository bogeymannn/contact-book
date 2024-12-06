# Load contacts from file
import csv

def load_from_file(filename="contacts.csv"):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader) 
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact list.")
        return []





# Save contacts to file
def save_to_file(contacts, filename="contacts.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['name', 'email', 'phone', 'address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
        print("Contacts saved to file.")