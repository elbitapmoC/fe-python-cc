textMessage = "Yo! I love huskies but they're so friggin hard to train. What's the next best option?!"
# THis is how we will slice the string, 0 starting point. 3 stoping point, it does NOT include index 3, it stops at 3.
majorKey = textMessage[0:3]
print(majorKey)

animal = 'catdog'
# print(animal[3:99])
# OR
# tells us I want to go to the end of the string.
print(animal[3:])  # dog

# From the beggining(0) all the way up to the entered index
print(animal[:3])  # cat

laughter = 'Ha!Ha!Ha!Ha!'
# print(laughter[0::2])
# Not too sure how this step is working, we'll comment out for now.

addy = """
chicken little
1284 Fort Knox Lane,
Nevada GA, 33333
"""

print(addy)
