while True:
    try:
        length = input("Podaj dlugosc miarki: ")
        length = int(length)

        unit = "|...."
        ruler = ""
        ruler_numbers = "0".ljust(5)
    
        for i in range(1, length + 1):
            ruler += unit
            sI=str(i)
            ruler_numbers += sI.ljust(6-len(sI))
        
        ruler += "| \n"
        ruler += ruler_numbers
        print(ruler)
    except ValueError:
        print("Error: To nie jest liczba calkowita")

    break