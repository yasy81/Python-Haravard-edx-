def main():
    time = input("What time is it? ")
    clock = convert(time)

    if 7 <= clock <= 8:
        print("breakfast time")
    if 12 <= clock <= 13:
        print("lunch time")
    if 18 <= clock <= 19:
        print("dinner time")
  
def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60


if __name__ == "__main__":
    main()
