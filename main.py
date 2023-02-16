import random

'''
A GOOD PASSWORD HAS THIS QUALITIES:
12 characters or more
mixed and matched caps, symbols, and numbers
no obvious subs (ex. @ for a, 3 for e)
not in dictionary
doesn't contain names
doesn't contain phone numbers or address'
unique (perhaps not necessary to code, user would be responsible for this part)
'''

# need to create a user input, rather than a hardset pass length
pass_min_len = int(input("Input password lenght (minimum of 6):"))

# special character set for better readability
special_characters = '!@#$%^&*'
possible_characters = 'qwertyuioplkjhgfdsamnbvcxzZXCVBNMASDFGHJKLPOIUYTREWQ0123456789' + special_characters

temp_password = []

if pass_min_len >= 6:
    for x in range(pass_min_len):
        random_char = random.choice(possible_characters)
        temp_password.append(random_char)
else:
    temp_password = "Password does not meet the minimum length."

password = ''.join(temp_password)

print(password)