#A breakpoint is simply a mechanism when using a text editor or an IDE that allows you to specify on what line or what lines of code do you want to pause or break execution of the program just so you can start poking around at that line of code.


def main():
    height = int(input("enter a number for the height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        #print(i, end = " ")
        print("#" * (i+1))

if __name__ == "__main__":
    main()
