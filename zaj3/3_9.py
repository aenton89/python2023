seq = []
while True:
    try:
        data = input("Podaj sekwencje liczb (oddziel elementy spacją) lub nacisnij Enter, aby zakonczyc: ")
        if not data:
            break
        elements = [int(e) for e in data.split()]
        seq.append(elements)
    except ValueError:
        print("Error: jeden z elementow to nie jest liczba, sprobuj ponownie")

seq_sum = [sum(s) for s in seq]
print("Sumy sekwencji:", seq_sum)