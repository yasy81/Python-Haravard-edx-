"""i = 3
while i != 0:
    print("meow")
    i = i-1

while i <= 3:
    print("meow")
    i = i+1

i = 0
while i < 3:
    print("meow")
    i = i+1

i = 0
while i <3:
    print("meow")
    i += 1

i = 0
while i <3:
    print("meow")
    i += 1

for i in [0,1,2]:
    print("meow")

for _ in range(1000):
    print("this is the best version")
    #instead of i you can use an underscore too if you won't be using the variable 

print("Meow"*3) #looks like a hungry cat...let's change it
print("Meow \n"*3)#it goes to the next line at the end we don't want that to happen lets fix it
print("Meow\n"*3, end="")



#I am not doing math I am meowing so it has to give me a positive value
n = int(input("what's n? "))
if n<0:
    n = int(input("what's n? "))
    if n<0:
        n = int(input("what's n? "))

#instead of this: infinite loop
while True:
    n = int(input("what's n? "))
    if n < 0:
        continue
    else:
        break

for _ in range(n):
    print("meow")
        
    



while True:
    n = int(input("what's n? "))
    if n>0:
        break

for _ in range(n):
    print("meow")

"""


def main():
    number = get_number()
    meow(number)
    
    

def get_number():
    while True:
       n = int(input("what's n? "))
       if n > 0:
           break
    return n 
       
       # if you use break to get out of the loop, but you need to hand back a value from a function,you still have to use the return keyword now
           
           

def meow(n):
    for _ in range(n):
        print("meow")

main()