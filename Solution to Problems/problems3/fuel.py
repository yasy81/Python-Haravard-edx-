def main():
    fraction = input("Fraction: ")
    fuel(fraction)
 
def fuel(x):
    while True:
        try:
            no1,no2 = list(map(int, x.split("/")))
            percentage = (no1/no2)*100
            if no1>no2:
                x = input("Fraction: ")
                continue
            elif percentage >= 99:
                print("F")
                break 
            elif percentage <= 1:
                print("E")
                break
            elif no1 <= no2:
                print(f"{(round(percentage))}%")
                break
            else:
               x = input("Fraction: ")
               continue 
        except ValueError:
            x = input("Fraction: ")
            continue
        except ZeroDivisionError:
            x = input("Fraction: ")
            continue


main()