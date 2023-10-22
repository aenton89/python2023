def dlugosc_wyrazow(napis):
    wyrazy = napis.split()
    dlugosci = [len(wyraz) for wyraz in wyrazy]
    suma_dlugosci = sum(dlugosci)
    return suma_dlugosci

def test():
    # Test 1:
    napis1 = "To jest test"
    assert dlugosc_wyrazow(napis1) == 10

    # Test 2:
    napis2 = ""
    assert dlugosc_wyrazow(napis2) == 0

    # Test 3:
    napis3 = """Tu mamy
    wiele wierszy"""
    assert dlugosc_wyrazow(napis3) == 18

    # Test 4:
    napis4 = "z kropka."
    assert dlugosc_wyrazow(napis4) == 8

    # Test 5:
    napis5 = "To        jest       napis"
    assert dlugosc_wyrazow(napis5) == 11

    print("test przeszedl pomyslnie")

test()