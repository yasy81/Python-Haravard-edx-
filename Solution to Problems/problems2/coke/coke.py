def main():
    Amount_Due = int(50)
    print("Amount Due: ", Amount_Due)
    machine(Amount_Due)

def machine(amountDue):
    amountDue = int(50)
    while amountDue>0:

        InsertCoin = int(input("Insert Coin: "))
        if InsertCoin in [5,10,25]:
            amountDue -= InsertCoin
            if amountDue >0:
                print("Amount Due:", amountDue)
        else:
            print("Amount Due:", amountDue)
            continue

        while amountDue<=0:
            print("Change Owed:", abs(amountDue))
            break
main()

