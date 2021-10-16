phonebook = {}

while True:
    action = input('Enter an action: ')  # show, add, get

    if action == 'show':
        for phone, name in phonebook.items():
            print(name, ':', phone)
    elif action == 'add':
        phone = input('Enter a phone number: ')
        name = input('Enter a name: ')
        phonebook[phone] = name
        print('Added!')
    elif action == 'get':
        phone = input('Enter a phone number: ')
        print('Name:', phonebook.get(phone, 'undefined'))
    elif action == 'del':
        phone = input('Enter a phone number: ')
        if phone in phonebook:
            del phonebook[phone]
            print('Deleted!')
        else:
            print('Number not found!')
    else:
        print('Undefined action!')

# for phone_name_item in phonebook.items():
#     phone = phone_name_item[0]
#     name = phone_name_item[1]
#     print(name, ':', phone)
