while True:
    try:
        x = input("Podaj liczbe rzeczywista (wpisz 'stop' aby zakonczyc): ")
        if x.lower() == 'stop':
            break
        x = float(x)
        x_3 = x ** 3
        print(f"x = {x}, x^3 = {x_3}")
    except ValueError:
        print("Error: To nie jest liczba rzeczywista, sprobuj ponownie.")