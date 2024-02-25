# Arbitrary Arguments, *args
"""
- If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
- Note:- This way the function will receive a tuple of arguments, and can access the items accordingly.
"""
def multipleInputs(*nums):
    print("Inputs given: ", nums)

multipleInputs("Amardeep", "Lokare", 1)

# Arbitrary Keyword Arguments, **kwargs
"""
- If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
- Note:- This way the function will receive a dictionary of arguments, and can access the items accordingly
"""
def keyvaluePair(**details):  # by ** we can give arguments in key-value paire.
    print(details.values())
    print(details.keys())
    print(details)

keyvaluePair(name="Amardeep", surname="Lokare", number=1)


# Lambda function In Python
"""
- A lambda function is a small anonymous function.
- A lambda function can take any number of arguments, but can only have one expression.
- Syntax:- lambda arguments : expression
"""

x = lambda a : a+10
print(x(5))

# The power of lambda is better shown when we use them as an anonymous function inside another function.
# Note:- Use lambda functions when an anonymous function is required for a short period of time.
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))