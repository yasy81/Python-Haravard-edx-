"""
x = input("what's x? ")
y = input("what's y? ")
print("concatenates them")
z = x + y #concatenates 
print(z)

#int is not only a type of data in python but it is also a function 
print("add them together")
z = int(x) + int(y)
print(z)

#instead of int you can use float too
x = float(input("what is x? "))
y = float(input("what is y? "))
print("round them up it they are float")
print(round(x+y))
#print(x+y)

#you want it to have commas ex: 1,000 or 1,000,000
#print(f"z") this would just print z 
print(f"{z:,}")

#float numbers only have a finite amount of memory
print("divide the two numbers and round them")
z=(round(x/y,2))
print(z)
print("The way you specify using an f string how many digits you want to print")
z = x/y
print(f"{z:.2f}")
print(z)

#so we can solve a problem in multiple ways 
"""

def main():
    x = int(input("enter a number: "))
    print("squared of x is ", square(x))

def square(n):
    return n * n
    #return pow(n,2) the first is the number the second one is the exponent

main()