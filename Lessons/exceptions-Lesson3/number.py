"""try:
    a = int(input("what's x? "))
    print(f"x is {a}")
except ValueError:
    print("x is not an integer ")


#name error if you enter a string as input: add else
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer ")
else:
    print(f"x is {x}")
"""

"""#more user friendly prompt the user again and again
while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer ")
    else:
        break

print(f"x is {x}")
"""
"""
while True:
    try:
        x = int(input("what's x? "))
        break
    except ValueError:
        print("x is not an integer ")
    

print(f"x is {x}")

"""
#If you're inventing your own function whose purpose in life isn't just a print something on the screen like a side effect but is to hand back a value, to hand you back a value,like on that same post-it note from our discussion of functions,well, you need to return x explicitly.

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        

main()
    
#Break is used to break out of loops. But it turns out that return is sort of stronger than break. It will not only break you out of a loop. It will also return a value for you.So it's doing two things for once, if you will.






