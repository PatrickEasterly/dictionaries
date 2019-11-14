# #given the following dictionary, representing a maping from names to phone numbers

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# # write code to:
# # print Elizabeth's phone number

# el = phonebook_dict['Elizabeth']
# print(el)

# # add an entry to the dictionary: Kareem: 938-489-1234
# phonebook_dict['Kareem'] = '938-489-1234'
# print(phonebook_dict['Kareem'])

# # delete Alice's phone entry

# del phonebook_dict['Alice']
# print(phonebook_dict)

# # change Bob's phone number to 968-345-2345
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict['Bob'])

# # print all the phone entries
# print(phonebook_dict.values())


# nested dictionaries

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#get the email addres of Ramit
# print(ramit['email'])

#get the first of Ramit's interests
# intr = ramit['interests'][0]
# print(intr)

# get the email address of jasmine
# print(ramit['friends'][0]['email'])

# get the second of Jan's intersts
# print(ramit['friends'][1]['interests'][1])


# letter summary
# write a letter histogram program that gets input and prints a dictionary with the tally of how many 
# times each letter in the alphabet was used in the word

user_input = input('Please enter a word: ')
alphabet = list('abcdefghijklmnopqrstuvwxyz')
def letter_histogram(word):
  