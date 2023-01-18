# age = int(input('Enter your age: '))

# if age > 65:
#     print('Hooblah! 🥤')
# elif age < 65 and age >= 21:
#     print('Cheers! 🍻')
# else:
#     print('No soup for you! 🧃')

fName = input('Enter your first name: ')
lName = input('Enter your first name: ')
total = len(fName) + len(lName)
if total > 12:
    print(f"{fName} {lName}, LONG!")
elif total == 12:
    print(f"{fName} {lName}, ON POINT!")
else:
    print(f"{fName} {lName}, SHORT!")

# Order of operations:
# not
# and
# or
