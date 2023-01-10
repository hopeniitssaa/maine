def rucsac(valoarea, volum, V):
    index = list(range(len(valoarea)))
    raport = [v / w for v, w in zip(valoarea, volum)]
    index.sort(key = lambda a: raport[a], reverse=True)
    max_valoarea = 0
    frac = [0] * len(valoarea)
    for a in index:
        if volum[a] <= V:
            frac[a] = 1
            max_valoarea += valoarea[a]
            V -= volum[a]
        else:
            frac[a] = V / volum[a]
            max_valoarea += valoarea[a] * V / volum[a]
            break
    return max_valoarea, frac
n = int(input("numarul de lucruri "))
valoarea = [150, 60, 80, 120, 180]
volum = [120, 40, 40, 100, 150]
V = 250
max_valoarea, frac = rucsac(valoarea, volum, V)
for a in range(len(frac)):
    print(f"încap {round(frac[a], 2)} lucruri, cu pretul de {valoarea[a]}")
print('suma valorilor lucrurilor=', max_valoarea)