menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

menu = {item.lower(): price for item, price in menu.items()}
    
def main():
    total_price = 0
    while True: 
        try:
            item = input("Item: ").lower()
            if item in menu:
                total_price += menu[item]
                print(f"Total: ${total_price:.2f}")
            
        except EOFError:
            
            break
        
        
    

main()