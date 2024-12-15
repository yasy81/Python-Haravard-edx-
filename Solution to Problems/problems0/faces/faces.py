def main():
    string = str(input())
    convert(string)


def convert(x):
     if ":)" in x:
         x = x.replace(":)", "🙂")
     if ":(" in x:
         x = x.replace(":(", "🙁")

     print(x)



main()

