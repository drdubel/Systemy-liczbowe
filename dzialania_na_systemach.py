DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def dec2cos(integer, radix=2):
    assert 2 <= radix <= len(DIGITS)
    digits = []
    a = integer
    while a > 0:
        a, reminder = divmod(a, radix)
        digits.append(DIGITS[reminder])
    digits.reverse()
    return "".join(digits)

def cos2dec(liczba, system=2):
    liczba = str(liczba)[::-1]
    wykonanie = 0
    wynik = 0
    for cyfra in liczba:
        wynik += system**wykonanie*int(DIGITS.index(cyfra))
        wykonanie += 1
    return wynik

def mnozenie(lic_1, lic_2, sys=10):
    return dec2cos(cos2dec(lic_1, sys) * cos2dec(lic_2, sys), sys)
    #lic_mnozona = max(lic_1, lic_2)
    #for _ in range(min(lic_1, lic_2)-1):
    #    lic_mnozona = dodawanie(lic_mnozona, max(lic_1, lic_2), sys)
    #return lic_mnozona

def dodawanie(lic_1, lic_2, sys=10):
    return dec2cos(cos2dec(lic_1, sys) + cos2dec(lic_2, sys), sys)
    #najw_znak = int(DIGITS[sys-1])
    #najw_lic = str(max(lic_1, lic_2))[::-1]
    #najm_lic = str(min(lic_1, lic_2))[::-1]
    #dododawania = najw_lic
    #suma = 0
    #for wyk in range(len(najw_lic)):
    #    if wyk >= len(najm_lic):
    #        print(wyk)
    #        if int(najw_lic[wyk]) > najw_znak:
    #            suma += (10+najw_znak-1)*(10**wyk)
    #        else:   
    #            suma += (int(najw_lic[wyk]))*(10**wyk)
    #    elif int(najm_lic[wyk]) + int(najw_lic[wyk]) > najw_znak:
    #        suma += (10+najw_znak-1)*(10**wyk)
    #        print("raz", (10+najw_znak-1)*(10**wyk))
    #    else:
    #        print("dwa", (int(najm_lic[wyk]) + int(najw_lic[wyk]))*(10**wyk))
    #        suma += (int(najm_lic[wyk]) + int(najw_lic[wyk]))*(10**wyk)
    #return suma

def odejmowanie(lic_1, lic_2, sys=10):
    return dec2cos(cos2dec(lic_1, sys) + cos2dec(lic_2, sys), sys)

def dzielenie(lic_1, lic_2, sys=10):
    pass

def potegowanie(lic_1, potega, sys=10):
    if potega == 0:
        return 1
    if potega < 0:
        return dzielenie(1, potega, sys)
    if potega%1:
        return "idz z tym do pierwiastkow"
    lic_wypotegowana = lic_1
    for _ in range(potega-1):
        lic_wypotegowana = mnozenie(lic_wypotegowana, lic_1, sys)
    return lic_wypotegowana

sy = 16
a = mnozenie(3, 10, sy)
b = odejmowanie("A1", a, sy)
print(dodawanie("A", b, sy))