import secrets
import string

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

# inputs for length of password. also, inputs for whether or not the individual may use special characters and punctuation. 
# pass_min_len = int(input("Input password lenght (minimum of 6):"))

while True:
    try:
        pass_min_len = int(input("Input password length (minimum of 6, recommendation of 12 or more):"))
        if pass_min_len < 6:
            raise ValueError("Password length must be at least 6.")
        break
    except ValueError as e:
        print("Error:", e, "Please try again.")

# spc_char_need = input("Can you have special characters in your password?(yes or no only):")
while True:
    try:
        spc_char_need = input("Can you have special characters in your password?(yes or no only):")
        spc_char_need = spc_char_need.lower()
        if spc_char_need != "yes" and spc_char_need != "no":
            raise ValueError("Must be a yes or no answer.")
        break
    except ValueError as e:
        print("Error:", e, "Please try again.")



# character list for possible characters. seperated special characters and punctuation for better readability.
possible_characters = string.ascii_letters + string.digits

# possible characters and if statements to create a list, then join into a string for further processing.
# possible_characters = [alphanumeric, ]

if spc_char_need == 'yes':
    possible_characters += string.punctuation

# temp password made to iterate through possible characters, then append into the password itself.
temp_password = []

# if pass_min_len >= 6:
for x in range(pass_min_len):
    random_char = secrets.choice(possible_characters)
    temp_password.append(random_char)
# else:
#     temp_password = "Password does not meet the minimum length."

password = ''.join(temp_password)

print(password)