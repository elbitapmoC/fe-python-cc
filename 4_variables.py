# Variable simply put allows us to put a name on our value. Anytime we'd like to use our value, simply reference it by it's name.
score = 0
score += 1
print(score)  # 1

# ---------
# BAD (variable does NOT start with number)
# 1stPlayer

# GOOD
# player_1

# ---------
# BAD(spacing in naming)
# player one

# GOOD
# player_one

# ---------
# BAD(make sure to not use keywords when naming your variable)
# help("keywords")

# GOOD
PI = 3.14159  # All caps indicate const to other developers
