def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    print(dollars)

def dollars_to_float(d):
    return float(d.replace("$", ""))
    


def percent_to_float(p):
    p = p.replace("%","")
    return float(p) / 100
    
    


main()