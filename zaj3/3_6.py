while True:
    try:
        length = input("Podaj dlugosc prostokata: ")
        length = int(length)
        width = input("Podaj szerokosc prostokata: ")
        width = int(width)

        rectangle = ""
    
        for i in range(2*length):
            if i % 2 == 0:
                line = "+---" * width + "+\n"
            else:
                line = "|   " * width + "|\n"
            rectangle += line
    
        rectangle += "+---" * width + "+\n"
        print(rectangle)

    except ValueError:
        print("Error: To nie jest liczba calkowita")

    break