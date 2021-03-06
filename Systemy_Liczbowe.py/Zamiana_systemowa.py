DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def dec2cos(integer, radix=2):
    assert 2 <= radix <= len(DIGITS)
    digits = []
    a = integer
    integer = str(integer)
    po_przec = 0
    if '.' in integer:
        a = integer[:integer.index('.')]
        po_przec = float(int(integer[integer.index('.')+1:])*10**(-1*len(integer[integer.index('.')+1:])))
    potega = -1
    a = int(a)
    while a > 0:
        a, reminder = divmod(a, radix)
        digits.append(DIGITS[reminder])
    digits.reverse()
    if po_przec:    
        digits.append('.')
    while po_przec != 0:
        if radix**potega <= po_przec:
            po_przec -= radix**potega
            digits.append('1')
        else:
            digits.append('0')
        potega -= 1
    return "".join(digits)

def cos2dec(liczba, system=2):
    lic_przed_kropka = 0
    liczba = str(liczba)[::-1]
    lic_po_kropce = liczba
    if '.' in liczba:
        msc_kropki = liczba.index('.')
        lic_po_kropce = liczba[msc_kropki+1:]
        lic_przed_kropka = liczba[:msc_kropki]
    wykonanie = 0
    wynik = 0
    lic_przed_kropka = str(lic_przed_kropka)[::-1]
    for cyfra in lic_po_kropce:
        wynik += system**wykonanie*int(DIGITS.index(cyfra))
        wykonanie += 1
    wykonanie = -1
    for cyfra_dalej in lic_przed_kropka:
        wynik += system**wykonanie*int(DIGITS.index(cyfra_dalej))
        wykonanie -= 1
    return wynik

print(dec2cos(612.03125, 2))