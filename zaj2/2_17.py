def posortuj_alfabetycznie_i_pod_wzgledem_dlugosci(napis):
    # sortowanie alfabetyczne
    wyrazy_alfabetycznie = sorted(napis.split())

    # sortowanie pod względem długości
    wyrazy_dlugosc = sorted(napis.split(), key=len)

    return wyrazy_alfabetycznie, wyrazy_dlugosc

def test():
    # Test 1:
    napis1 = "jabko truskawka gruszka pomarancza"
    alfabetycznie1, dlugosc1 = posortuj_alfabetycznie_i_pod_wzgledem_dlugosci(napis1)
    assert alfabetycznie1 == ["gruszka", "jabko", "pomarancza", "truskawka"] and dlugosc1 == ["jabko", "gruszka", "truskawka", "pomarancza"]

    # Test 2:
    napis2 = ""
    alfabetycznie2, dlugosc2 = posortuj_alfabetycznie_i_pod_wzgledem_dlugosci(napis2)
    assert alfabetycznie2 == [] and dlugosc2 == []

    # Test 3:
    napis3 = "Python"
    alfabetycznie3, dlugosc3 = posortuj_alfabetycznie_i_pod_wzgledem_dlugosci(napis3)
    assert alfabetycznie3 == ["Python"] and dlugosc3 == ["Python"]

    # Test 4:
    napis4 = "python java"
    alfabetycznie4, dlugosc4 = posortuj_alfabetycznie_i_pod_wzgledem_dlugosci(napis4)
    assert alfabetycznie4 == ["java", "python"] and dlugosc4 == ["java", "python"]

    print("test przeszedl pomyslnie")

test()