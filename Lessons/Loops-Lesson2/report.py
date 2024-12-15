def main():
    #first way to add to dictionaries 
    #spacecraft = {"Name":"Arcade", "Distance": 168}

    #first way to add to dictionaries second way to add to dictionaries
    """spacecraft = {"Name":"James Web Space Telescope"}
    spacecraft["Distance"] = 0.01"""

    #If I wanted to add not just one key at a time to my dictionary,but maybe multiple at once, I could use a method called update.
    spacecraft = {"Name":"James Web Space Telescope"}
    spacecraft.update({"Distance": 0.01, "orbit":"sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""

    ===========report============

    Name: {spacecraft.get("Name","Unknown")}
    Distance: {spacecraft.get("Distance", "Unknown")}
    orbit: {spacecraft.get("orbit","Unknown")}

    =============================
    """
    #Name: {spacecraft["Name"]}
    #Distance: {spacecraft["Distance"]} AU instead of this you could write the distance like above..so that just incase there is no distance value it will return Unknown

main()