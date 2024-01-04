contacts = []

def display_menu():
    print("Menu")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. List of all contacts")
    print("6. Exit")

def add_contact():
    name = input("Enter the contact's name: ")
    email = input("Enter the contact's email: ")
    phone = input("Enter the contact's phone number: ")
    contact = {"Name": name, "Email": email, "Phone": phone}
    contacts.append(contact)   
    print("Contact added successfully!")
def search_contact():
    search_con = input("Enter the name or email of the contact to search: ") 
    found_contacts = []  
    for contact in contacts:
        if search_con.lower() in contact["Name"].lower() or search_con.lower() in contact["Email"].lower():
            found_contacts.append(contact)  

    if found_contacts:  
        print("Matching contacts found:")
        for contact in found_contacts: 
            print("Name:", contact["Name"])
            print("Email:", contact["Email"])
            print("Phone:", contact["Phone"])
            print("*******************")
    else:
        print("No matching contacts found.")

def update_contact():    
    name = input("Enter the name of the contact to update: ")
    found_contact = None 
    for contact in contacts: 
        if contact["Name"].lower() == name.lower():
            found_contact = contact 
            break

    if found_contact:  
        print("Contact found. Enter new details:")
        found_contact["Name"] = input("Enter the new name: ")
        found_contact["Email"] = input("Enter the new email: ")
        found_contact["Phone"] = input("Enter the new phone number: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")  
    for contact in contacts: 
        if contact["Name"].lower() == name.lower():  
            contacts.remove(contact)  
            print("Contact deleted successfully!")
            break
    else:
        print("Contact not found.")

def display_all_contacts():
    if contacts:
        print("All Contacts:")
        for contact in contacts:   
            print("Name:", contact["Name"])
            print("Email:", contact["Email"])
            print("Phone:", contact["Phone"])
            print("***********************") 
    else:
        print("No contacts found.")

#main program starts here
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        print("Program has ended")
        break 
    else:
        print("Invalid choice")
