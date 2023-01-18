
def get_units():
    temp_unit = input(
        'What unit are you using for the temperature (F, C or K)? ')
    return temp_unit.upper()


def get_temp():
    temp_temp = input('What temp is the water at? ')
    return temp_temp


def checkTemp():
    if (units == 'F'):
        if (temp < 212):
            print('BOILING!')
        else:
            print('COOLIN')
    elif (units == 'C'):
        if (temp < 100):
            print('BOILING!')
        else:
            print('COOLIN')
    elif (units == 'K'):
        if (temp < 373):
            print('BOILING!')
        else:
            print('COOLIN')


units = get_units()
while (units != 'F' or units != 'C' or units != 'K'):
    print("Try again, make sure you enter: 'F', 'C' or 'K'.")
    units = get_units()

temp = get_temp()
while ((type(temp) != int)):
    print("Try again, make sure you're entering a NUMBER.")
    temp = get_temp()

# f - 212
# c - 100
# k - 373
