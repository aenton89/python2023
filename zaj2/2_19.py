def zbuduj_napis_z_blokami(L):
    bloki = [str(liczba).zfill(3) for liczba in L]
    napis = ''.join(bloki)
    return napis

def test():
    # Test 1:
    L1 = [7, 24, 111, 5, 0]
    assert zbuduj_napis_z_blokami(L1) == "007024111005000"

    # Test 2:
    L2 = []
    assert zbuduj_napis_z_blokami(L2) == ""

    # Test 3:
    L3 = [9]
    assert zbuduj_napis_z_blokami(L3) == "009"

    # Test 4:
    L4 = [123, 456, 789]
    assert zbuduj_napis_z_blokami(L4) == "123456789"

    print("test przeszedl pomyslnie")
    
test()