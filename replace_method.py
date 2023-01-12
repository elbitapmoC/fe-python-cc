races = '3kilometers 5kilometers 10kilometers 41kilometers'
print(races.replace('kilometers', 'km'))

prices = '$1.99 $2.99 $3.99 $4.99 $6.99 $9.99'
# Passing a third value limits the amount out times a character is replaced.
print(prices.replace('$', '', 3))
