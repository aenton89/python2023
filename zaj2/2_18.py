def liczba_zer_w_liczbie(liczba):
    liczba_str = str(liczba)

    liczba_zer = liczba_str.count('0')
    
    return liczba_zer

def test():
    # Test 1:
    liczba1 = 102030405060
    assert liczba_zer_w_liczbie(liczba1) == 6

    # Test 2:
    liczba2 = 123456789
    assert liczba_zer_w_liczbie(liczba2) == 0

    # Test 3:
    liczba3 = 100
    assert liczba_zer_w_liczbie(liczba3) == 2

    # Test 4:
    liczba4 = 100001000
    assert liczba_zer_w_liczbie(liczba4) == 7

    print("test przeszedl pomyslnie")

test()