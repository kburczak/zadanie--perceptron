import random

class Perceptron:
    def __init__(self, ilosc):
        self.ilosc = ilosc
        self.wagi = [random.uniform(0, 1) for _ in range(ilosc + 1)]

    def perceptron_update(self, x):
        for krok in range(self.ilosc, len(x)):
            wejscia = x[krok - self.ilosc:krok]
            oczekiwany = x[krok]
            predkosc_uczenia = 0.001

            for _ in range(10000):
                przewidywany = sum(waga * wejscie for waga, wejscie in zip(self.wagi, wejscia)) + self.wagi[-1]
                blad = oczekiwany - przewidywany
                self.wagi = [waga + wejscie * blad * predkosc_uczenia for waga, wejscie in zip(self.wagi, wejscia)] + [self.wagi[-1] + 1 * blad * predkosc_uczenia]

        return self.wagi

    def perceptron_predict(self, x):
        for krok in range(self.ilosc, len(x)):
            wejscia = x[krok - self.ilosc:krok]
            oczekiwany = x[krok]
            przewidywany = sum(waga * wejscie for waga, wejscie in zip(self.wagi, wejscia)) + self.wagi[-1]
            print(f'przewidywany {przewidywany} faktyczny {oczekiwany}')


eur = 100
usd = 100
eur_to_usd = []
trend = 0
z_5 = 0
ilosc = 0

git remote add origin https://github.com/kburczak/zadanie--perceptron.git

for ilosc in range(1, 99):
    nowy = float(input())
    eur_to_usd.append(nowy)
    ilosc = ilosc+1

perceptron = Perceptron(ilosc)

perceptron.perceptron_update(eur_to_usd)
perceptron.perceptron_predict(eur_to_usd)
print(eur_to_usd)
print(f'wagi: {perceptron.wagi}')