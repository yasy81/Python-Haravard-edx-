months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# input =  (MM/DD/YYYY)  output = YYYY-MM-DD
def main():
    while True:
        date = input("")
        if "/" in date:
            x = date.split("/")
        else:
            x = date.split()
            


main()

