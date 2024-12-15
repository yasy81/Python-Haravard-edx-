def main():
    expression = input("Expression: " )
    x,y,z = expression.split()
    x = int(x)
    z = int(z)
    result = operators(x,y,z )
    print(result)

def operators(x,y,z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    

main()