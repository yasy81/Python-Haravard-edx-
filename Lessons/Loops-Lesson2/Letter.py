def main():
   
   """ print(write_letter("Caleb","Sara"))
    print(write_letter("Mahsa","Sara"))
    print(write_letter("Taylor","Sara"))
    print(write_letter("Elina","Sara"))

    """
    #instead we could make a list 
   names = ["Mario", "Luigi", "Daisy","Yoshi","nikki","jikili","blabla","Alo"]
   """for i in range(len(names)):
       print(write_letter(names[i],"Sara"))
       """
   for name in names:
       print(write_letter(name,"Sara"))
       ...
    


def write_letter(receiver,sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    dear {receiver},

     I am looking forward to see you in 
     the ball at 8:00 PM in the musiam 
     hall

    sincerely,
     {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+


    """
main()