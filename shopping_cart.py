# METHOD 1

# print("""
# WELCOME TO OUT USELESS STORE!
# *****************************
# """)
# itemName = input("What item are you purchasing? ")
# itemPrice = input(f"What is the price of {itemName}? ")
# itemAmount = input(f"How many {itemName}(s) are you buying? ")
# fullString = (f"Added {itemAmount} {itemName}(s) to shopping cart.\n"
#               f"Subtotal: ${int(itemPrice) * int(itemAmount)}")
# print(fullString)


# METHOD 2

print("""
WELCOME TO OUT USELESS STORE!
*****************************
""")
itemName = input("What item are you purchasing? ")
itemPrice = float(input(f"What is the price of {itemName}? "))
itemAmount = float(input(f"How many {itemName}(s) are you buying? "))
fullString = (f"Added {itemAmount} {itemName}(s) to shopping cart.\n"
              f"Subtotal: ${itemPrice * itemAmount}")
print(fullString)
