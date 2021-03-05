def trzyliterowe_napisy(ulamek):
    ulamek = ulamek.split()
    ulamek_wym = int(ulamek[0])/int(ulamek[1])
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    listo_szyfr = [
        ["a", "b", "c", "d", "e", "f"], 
        ["g", "h", "i", "j", "k"], 
        ["l", "m", "n", "o", "p"], 
        ["q", "r", "s", "t", "u"], 
        ["v", "w", "x", "y", "z"]
    ]
    wyk = 0
    komb = []
    while True:
        
        wyk += 1
        if wyk >= len(alfabet):
            break

print(trzyliterowe_napisy('3 3'))