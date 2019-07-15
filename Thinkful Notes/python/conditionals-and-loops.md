# Working with conditional statements and loops


The following comes directly from Thinkful.
``` python
def greet_admin(user):
    if user == "Guido":
        return "Welcome, Guido."
    elif user == "Bethany":
        return "Welcome, Bethany."
    elif user == "Alex":
        return "Welcome, Alex."
    else:
        return "You are not authorized."
```

Use **for** loops whenever there is a block of operations that you want to perform on each value in a set of values, or when you want to perform a specific number of times. 

``` python
even_numbers = []
odd_squares = []

for n in range(10):
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_squares.append(n ** 2)

print(even_numbers)
print(odd_squares)

```
