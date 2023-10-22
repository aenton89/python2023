def najdluzszy_wyraz_i_dlugosc(napis):
    wyrazy = napis.split()
    
    if not wyrazy:
        return None, 0  # gdy napis jest pusty

    najdluzszy_wyraz = max(wyrazy, key=len)
    dlugosc = len(najdluzszy_wyraz)
    return najdluzszy_wyraz, dlugosc

def test():
    # Test 1:
    napis1 = "to jest testowy napis."
    wyraz1, dlugosc1 = najdluzszy_wyraz_i_dlugosc(napis1)
    assert wyraz1 == "testowy" and dlugosc1 == 7

    # Test 2:
    napis2 = ""
    wyraz2, dlugosc2 = najdluzszy_wyraz_i_dlugosc(napis2)
    assert wyraz2 is None and dlugosc2 == 0

    # Test 3:
    napis3 = """kolejny, ktory
    ma wiele """
    wyraz3, dlugosc3 = najdluzszy_wyraz_i_dlugosc(napis3)
    assert wyraz3 == "kolejny," and dlugosc3 == 8

    # Test 4:
    napis4 = "jeden"
    wyraz4, dlugosc4 = najdluzszy_wyraz_i_dlugosc(napis4)
    assert wyraz4 == "jeden" and dlugosc4 == 5

    # Test 5:
    napis5 = "To        jest       napis."
    wyraz5, dlugosc5 = najdluzszy_wyraz_i_dlugosc(napis5)
    assert wyraz5 == "napis." and dlugosc5 == 6

    print("test przeszedl pomyslnie")
    
test()