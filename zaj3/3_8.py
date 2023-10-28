seq1 = input("Podaj pierwsza sekwencje (oddziel elementy spacja): ").split()
seq2 = input("Podaj druga sekwencje (oddziel elementy spacja): ").split()

mutual_el = list(set(seq1) & set(seq2))
all_el = list(set(seq1) | set(seq2))

print("Wspolne elementy:", mutual_el)
print("Wszystkie elementy:", all_el)