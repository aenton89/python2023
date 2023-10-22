def liczba_wyrazow(napis):
    wyrazy = napis.split()
    return len(wyrazy)

def test():
    # Test 1
    napis1 = "sprawdzam ten test"
    assert liczba_wyrazow(napis1) == 3

    # Test 2
    napis2 = ""
    assert liczba_wyrazow(napis2) == 0

    # Test 3
    napis3 = """wiele wierszy sprawdzam, raz
    dwa trzy cztery"""
    assert liczba_wyrazow(napis3) == 7

    # Test 4:
    napis4 = "tak        nie       moze."
    assert liczba_wyrazow(napis4) == 3

    # Test 5:
    napis5 = "slowo"
    assert liczba_wyrazow(napis5) == 1

    print("test przeszedl pomyslnie")

test()