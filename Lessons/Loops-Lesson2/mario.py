"""def main():
    print_column(3)

def print_column(height):
    print("#\n"*height, end = "")
    #for _ in range(height): print("#")

main()"""

"""def main():
    print_row(3)

def print_row(width):
    print("?"*width)

main()"""

#two dimensional 

def main():
    print_square(10)

def print_square(size):
    for i in range(size):
      print_row(size)

def print_row(width):
    print("#"*width)


"""def print_square(size):
    for i in range(size):
        print("#"*size)
        """
"""
def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row 
        for j in range(size):
            #print brick
            print("#", end = "")
            # I don't want a newline after each brick I need one after each row
        print()"""



main()