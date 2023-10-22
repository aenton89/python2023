def rozdziel_znaki_napisu(napis):
    return "_".join(napis)

def test():
    # Test 1:
    napis1 = "Python"
    assert rozdziel_znaki_napisu(napis1) == "P_y_t_h_o_n"

    # Test 2:
    napis2 = "sprawdzam"
    assert rozdziel_znaki_napisu(napis2) == "s_p_r_a_w_d_z_a_m"

    # Test 3:
    napis3 = ""
    assert rozdziel_znaki_napisu(napis3) == ""

    # Test 4:
    napis4 = "k"
    assert rozdziel_znaki_napisu(napis4) == "k"

    # Test 5:
    napis5 = "  S p a c j e  "
    assert rozdziel_znaki_napisu(napis5) == " _ _S_ _p_ _a_ _c_ _j_ _e_ _ "

    print("test przeszedl pomyslnie")

test()