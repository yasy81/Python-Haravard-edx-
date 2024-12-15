from collections import Counter

def main():
    groceries = []
    while True:
        try: 
            grocery = input("").upper()
            groceries.append(grocery)
        except EOFError:
            break

    groceries.sort()
    word_counts = Counter(groceries)
    for word, count in word_counts.items():
        print(f"{count} {word}")

main()
