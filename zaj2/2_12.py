def pierwsze_znaki_wyrazow(napis):
    wyrazy = napis.split()
    pierwsze_znaki = [wyraz[0] for wyraz in wyrazy]
    return ''.join(pierwsze_znaki)

def ostatnie_znaki_wyrazow(napis):
    wyrazy = napis.split()
    ostatnie_znaki = [wyraz[-1] for wyraz in wyrazy]
    return ''.join(ostatnie_znaki)

def test_pierwsze_znaki_wyrazow():
    # Test 1:
    napis1 = "to tylko przyklad"
    assert pierwsze_znaki_wyrazow(napis1) == "ttp"

    # Test 2:
    napis2 = ""
    assert pierwsze_znaki_wyrazow(napis2) == ""

    # Test 3:
    napis3 = "Python"
    assert pierwsze_znaki_wyrazow(napis3) == "P"

    # Test 4:
    napis4 = "A   B  C"
    assert pierwsze_znaki_wyrazow(napis4) == "ABC"

    print("test pierwszy przeszedl pomyslnie")

def test_ostatnie_znaki_wyrazow():
    # Test 1:
    napis1 = "to tylko przykład"
    assert ostatnie_znaki_wyrazow(napis1) == "ood"

    # Test 2:
    napis2 = ""
    assert ostatnie_znaki_wyrazow(napis2) == ""

    # Test 3:
    napis3 = "Python"
    assert ostatnie_znaki_wyrazow(napis3) == "n"

    # Test 4:
    napis4 = "A   B  C"
    assert ostatnie_znaki_wyrazow(napis4) == "ABC"

    print("test drugi przeszedl pomyslnie")

test_pierwsze_znaki_wyrazow()
test_ostatnie_znaki_wyrazow()