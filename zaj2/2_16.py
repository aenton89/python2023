def zamien_GvR_na_nazwisko(line):
    line_zamieniony = line.replace("GvR", "Guido van Rossum")
    return line_zamieniony

def test():
    # Test 1:
    line1 = "GvR jest tworca Pythona."
    assert zamien_GvR_na_nazwisko(line1) == "Guido van Rossum jest tworca Pythona."

    # Test 2:
    line2 = "python to jezyk programowania."
    assert zamien_GvR_na_nazwisko(line2) == "python to jezyk programowania."

    # Test 3:
    line3 = "GvR to GvR i jeszcze raz GvR."
    assert zamien_GvR_na_nazwisko(line3) == "Guido van Rossum to Guido van Rossum i jeszcze raz Guido van Rossum."

    # Test 4:
    line4 = ""
    assert zamien_GvR_na_nazwisko(line4) == ""

    print("test przeszedl pomyslnie")

test()