# Working with Strings

The following example is taken directly from Thinkful. 
``` python
# Return a new string with a capitalized first character.
'hello'.capitalize()

# As you read through these make a guess about what the result
# will be, then check your guess by `print()`ing each statement
# and running the code.
print('hello'.capitalize())

# Return a new string where all characters are lower case
'Hello'.lower()
'WORLD'.lower()

# Check whether all characters are numeric.
'1337'.isdecimal()
'p2p'.isdecimal()

# Check whether all characters are alpha.
'hello'.isalpha()
'p2p'.isalpha()

# Find the index of the first occurance of a substring. 
'hello'.find('l')
'world'.find('l')

# Check the end of a string.
'hello'.endswith('o')
'world'.endswith('o')
'world'.endswith('rld')

# Split a string into a list of strings at each instance of a
# substring.
'The-quick-brown-fox'.split('-')

# Join a list of strings into one single string. Try passing a
# different string into this method.
'_'.join(['The', 'quick', 'brown', 'fox'])

# "Format" a string by replacing `{}` with the arguments you
# supply to the function.
'Player {} has {} hit points remaining'.format(1, 42)
'My favorite drink is {} with {} dashes of {}'.format('whiskey', 3, 'bitters')

# Use the space below to play around with these methods and print
#different things out.
```
