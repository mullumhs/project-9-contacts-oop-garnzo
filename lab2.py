"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.
class Contact:
    number_of_contacts = 0

    def __init__(self, name, ph_number):
        self.name = name
        self.ph_number = ph_number
        Contact.number_of_contacts += 1

# Create at least two instances of the Contact class with different data.   
contact1 = Contact("Jeff", "0401 736 925")
contact2 = Contact("Bill", "0487 873 173")

# Write code that prints out the details of each contact you have created.
print(contact1.name, contact1.ph_number)
print(contact2.name, contact2.ph_number)    



