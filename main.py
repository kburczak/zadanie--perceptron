
def perceptron_update(x):
    for krok in range(0, len(x)):
        wagi = [0.1, -0.3, 0.5, 0.8]
        wejscia = [x[krok], x[krok+1], x[krok+2]]
        wejscia = x
        oczekiwany = 56
        oczekiwany = x[krok+4]
        predkosc_uczenia = 0.001


        for i in range(0, 1):
            przewidywany = wagi[0] * wejscia[0] + wagi[1] * wejscia[1] + wagi[2] * wejscia[2] + wagi[3] * 1
            blad = oczekiwany - przewidywany
            wagi = [(wagi[0] + wejscia[0]) / blad, (wagi[1] + wejscia[1]) / blad, (wagi[2] + wejscia[2]) / blad, (wagi[3] + 1) / blad]

    return wagi

eur = 100
usd = 100
eur_to_usd = []
trend = 0
z_5 = 0

for ilosc in range(1, 100):
    nowy = input()
    eur_to_usd.append(nowy)

wagi = perceptron_update(nowy)
print(wagi)
"""for i in range(1, len(eur_to_usd)):
    if eur_to_usd[i] > eur_to_usd[i - 1]:
        if trend < 0:
            trend = 0
        trend = trend + 1
    elif eur_to_usd[i] < eur_to_usd[i - 1]:
        if trend > 0:
            trend = 0
        trend = trend - 1
    if i >= 5:
        for a in range(i - 5, i):
            if eur_to_usd[a] > eur_to_usd[a - 1]:
                z_5 = z_5 + 1
            elif eur_to_usd[a] < eur_to_usd[a - 1]:
                z_5 = z_5 - 1

    if z_5 == 0:
        if trend > 0:
            eur = eur + usd / eur_to_usd[i]
            usd = 0
        elif trend < 0:
            usd = usd + eur * eur_to_usd[i]
            eur = 0
    else:
        if z_5 < 0:
            eur = eur + usd / eur_to_usd[i]
            usd = 0
        elif z_5 > 0:
            usd = usd + eur * eur_to_usd[i]
            eur = 0

print("całość na początku w dolarach", 100 + 100 * eur_to_usd[0])
print("całość na początku w euro", 100 + 100 / eur_to_usd[0])

print(f'euro: {eur}')
print(f'dolary: {usd}')"""

    #print(przewidywany)
    #print(blad)
    #print(wagi)