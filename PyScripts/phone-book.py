import re, os, sys

# Create phone book directory
# Add contact and phone number to text directory
# Use sys.argv to search for names and provide output

def addContact(phoneBook):
    while True:
        prompt = input('Do you want to add a contact[Y/N]? ')
        if prompt == 'Y':
            contact = input('Contact Name: ')
            phoneNum = input('Phone: ')
            phoneBook.write('Contact: ' + contact + '\n' + 'Phone: ' + phoneNum + '\n-----------\n')
            phoneBook.close()
            print('Contact: ' + contact + ' ' + 'Phone: ' + phoneNum)
        elif prompt == 'N':
            prompt2 = input('Would you like to print the current Phone Book Directory[Y/N] ')
            if prompt2 == 'Y':
                phoneBook = open('phonebook.txt')
                content = phoneBook.read()
                phoneBook.close()
                print(content)
                return
            elif prompt2 == 'N':
                print('\nGoodbye!\n')
                return
        else:
            print('\nPlease type Y, N, or Ctrl-C to quit.\n')


# TODO - Make input into dictionary so that contact name can be called based on Key Value pair
# TODO - Figure out Ctrl-C KeyboardInterrupt code
# TODO - Figure out how to loop Contact Adds
# TODO - Add .Bat code
  
# Call Function to add contact info
document = open('phonebook.txt', 'a')
content = addContact(document)

