def napis_z_liczb(L):
    napis = ''.join(str(x) for x in L)
    return napis

def test():
    # Test 1:
    L1 = [1, 2, 3, 4, 5]
    assert napis_z_liczb(L1) == "12345"

    # Test 2:
    L2 = [9]
    assert napis_z_liczb(L2) == "9"

    # Test 3:
    L3 = []
    assert napis_z_liczb(L3) == ""

    # Test 4:
    L4 = [10, 20, 30, 40, 50]
    assert napis_z_liczb(L4) == "1020304050"

    print("test przeszedl pomyslnie")

test()