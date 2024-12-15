distances = {
    "Voyager 1" : 163,
    "Voyager 2" : 180,
    "voyager 3" : 176,
    "Voyager 11": 156
}

def main():

    for distance in distances.values():
        print(f"{distance} AU is {converted_distance(distance)} m" )
    #if you use values() instead of keys it will return the values without their corresponding keys
    """
    for value in distances.values():
        print(values)
    """
    #using keys
    """for name in distances.keys():
        print(f"{name} is {distances[name]} AU from earth")
"""
def converted_distance(au):
    return au * 149597870700

main()



