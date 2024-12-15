string = input("Enter greeting: ").strip()
first_letter = string[0].lower()

if string.lower().startswith("hello"):
    print("$0")
elif first_letter == "h":
    print("$20")
else:
    print("$100")

