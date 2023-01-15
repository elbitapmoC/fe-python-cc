tweet = input("What's on your mind? Tweet about it: ")
MAX_CHARS = 140
MIN_CHARS = 12

if len(tweet) > MAX_CHARS:
    print(f"Your tweet is {len(tweet) - MAX_CHARS}, character(s) too long.")
elif (len(tweet) < MIN_CHARS):
    print(f"Your tweet is {MIN_CHARS - len(tweet)}, character(s) too short.")
else:
    print(f"{tweet} ({len(tweet)} characters)")
