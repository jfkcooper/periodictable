from periodictable import H, O, Fe, helium, elements

def test():
    # Check that we can access element properties
    assert H.name == "hydrogen"
    assert H.symbol == "H"
    assert H.number == 1
    assert helium.symbol == 'He'

    # Check that isotopes work and produce the correct strings and symbols
    O.add_isotope(18)
    assert H[2].symbol == 'D'
    assert H[3].symbol == 'T'
    assert O[18].symbol == 'O'
    assert str(H[2])=='D'
    assert str(H[3])=='T'
    assert str(O[18])=='18-O'

    # Check that "for el in elements" works and for iso in el works
    els = tuple(el for el in elements)
    assert els[0].number == 0
    assert els[1].number == 1
    isotopes = tuple(iso for iso in O)
    assert isotopes[0].isotope == 12  # 12 is the first oxygen isotope listed

    # Check that table lookup works and fails appropriately
    Fe.add_isotope(56)
    assert elements.symbol('Fe') == Fe
    assert elements.name('iron') == Fe
    assert elements.isotope('Fe') == Fe
    assert elements.isotope('56-Fe') == Fe[56]
    try:
        elements.symbol('Qu')
    except ValueError,msg:
        assert str(msg) == "unknown element Qu"
    try:
        elements.name('Qu')
    except ValueError,msg:
        assert str(msg) == "unknown element Qu"
    try:
        elements.isotope('Qu')
    except ValueError,msg:
        assert str(msg) == "unknown element Qu"

if __name__ == "__main__": test()
