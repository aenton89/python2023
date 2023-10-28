''' inny sposob tworzenia slownika:
rom_v = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arab_v = [1, 5, 10, 50, 100, 500, 1000]

rom_arab = dict(zip(rom_v, arab_v))
'''

def roman2int(rom_nb):
    rom_arab = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    sum = 0
    last_value = 0

    for symbol in reversed(rom_nb):
        value = rom_arab[symbol]
        if value < last_value:
            sum -= value
        else:
            sum += value
        last_value = value

    return sum


while True:
    rom_nb = input("Podaj liczbe w zapisie rzymskim(lub nacisnij Enter, zeby zakonczyc): ")
    if not rom_nb:
        break
    result = roman2int(rom_nb)
    print(f"{rom_nb} = {result}")