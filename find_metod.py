people = 'Johnny Nomo Appolseed III'
print(people.find('y'))  # index of 5 returned

# 2nd argument is the starting point.
print(people.find('o', 11))  # index of 15 returned

# 3rd argument is the ending point.
print(people.find('o', 7, 10))  # index of 10 returned
