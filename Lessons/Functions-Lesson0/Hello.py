name = input("what's your name? ")
#name = input("what's your name? ").strip().title() you can write them you one line
#.strip().title() can only be used for strings and not functions (unless your function returns a string)
print("hello,", name )
print("hello, "+ name )
#the next two print options are being printed in one line
print("hello,", end = " ")
print(name)

print("hello", name, sep = "???")
#function is an action or word that we use to get the computer to do those things 
# print is a function 
#argument is an input to a function that somehow influences it's behavior 
#hello world here is known as a side effect 
#return values
#So in Python and many programming languages,
#a single equal sign is the assignment operator and what that means specifically is that, you want to assign from right to left whatever the user's input is.

#code Hello.py (this did not work in the terminal)

#quotation marks in the print 
print("Hello, \"Friend\"")
print('Hello, "Friend"')
#removes the whitespaces from the input 
name = name.strip()
#capitalize the name
name = name.capitalize()
#capitalizes the first letter of each word
name = name.title()
#name = name.strip().title()
#format string 
print(f"Hello, {name}")

#split user name into first name and last name
#first, last = name.split(" ")
#print(f"hello, {first}")

print("using a hello function:.....")
#name is compied into another variable called 
def hello(to="world"):
    print("hello, ", to)
hello()
hello(name)


print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="World"):
    print("hello, ", to)

main()


#scope refers to the variable only existing in the context in which you defined it
"""
def main():
    name = input("whats your name? ")
    hello()

def hello(to="world")
    print("hello", name)

main()

NameError: name 'name' is not defined
"""

# https://docs.python.org/3/library/functions.html#input

# https://docs.python.org/3/library/stdtypes.html#string-methods


