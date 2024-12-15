name = input("Whats your name? ")

"""
if name == "Harry": 
    print("Gryffindor")
elif name == "Harmonie":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else: 
    print("Who?")
"""

"""
if name == "Harry" or name == "Harmonie" or name == "Ron": 
    print("Gryffindor")

elif name == "Draco":
    print("Slytherin")
else: 
    print("Who?")
"""

"""
match name:
    case "Harry": 
        print("Gryffindor")
    case "Harmonie":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: 
        print("Who? ")
"""

match name:
    case "Harry"| "Harmonie"| "Ron": 
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: 
        print("Who? ")



