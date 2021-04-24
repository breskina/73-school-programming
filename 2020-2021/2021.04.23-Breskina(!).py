while True:
    a=float(input("a="))
    b=float(input("b="))
    if a<b:
        print ("a<b")
    elif a==b:
        print ("a=b")
    else:
        print ("a>b")

    print ("Приємно було, що Ви скористалися нашою прогармою")
    exit=input("Якщо Ви хочете \n   закічнити роботу з програмою -  введіть 1,\n   продовжити - введіть інше число: ")
    if exit=="1":
        quit()


