# Kids drink toddy.
# Teens drink coke.
# Young adults under drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky"

# Input of an age -> integer
# Output -> string - "drink ______"

# Look at input integer
# Determine what age group it falls under
    #0-14 -> child
    # 14-17 -> Teen
    #18-20 - > Young adult
    # 21+ -> adult
# Once I have determined age group, determine drink choice
#return string with word "drink" and "drink_choice"


def solution(age):
    if age < 14:
        drink_choice = 'toddy'
    elif age < 18:
        drink_choice = 'coke'
    elif age < 21:
        drink_choice = 'beer'
    else:
        drink_choice = 'Whisky'
    return 'drink' + drink_choice

