def main():
    camalCase = input("camalCase: ")
    output = snake_case(camalCase)
    print("snake_case: ", output)
def snake_case(s):
    snake = ""
    for char in s:
        if char.isupper():
            snake += "_"
        snake += char.lower()
    return snake


main()