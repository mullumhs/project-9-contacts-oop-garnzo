"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contacts
class Contact:
    number_of_contacts = 0

    def __init__(self, name, ph_number, email):
        self.email = email
        self.name = name
        self.ph_number = ph_number
        Contact.number_of_contacts += 1

    def check_email(self):
        if "@" in self.email:
            print(f"{self.name}'s email is valid")
            return True
        else:
            print(f"{self.name}'s email is invalid")
            return False
        
contact1 = Contact("Jeff", "0401 736 925", "jeff@gmail.com")
contact2 = Contact("Bill", "0487 873 173", "poppy@gmail.com")

contact1.check_email()