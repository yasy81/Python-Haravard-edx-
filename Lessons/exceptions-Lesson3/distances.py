distances = {
    "Voyager 1" : "163",
    "Voyager 2" : "180",
    "voyager 3" : "176",
    "Voyager 11": "44 AU" #it can't turn AU into a float

}

def main():

    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"the spacecraft {spacecraft} is not in the dictionary")
        return
    except ValueError:
        print(f"can't convert '{distances[spacecraft]}' to a float")
        return
    
    print(f"m is {m} away")
    m = convert(au)
 

def convert(au):
    return au * 149597870700

main()



