# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 00:20:39 2021

@author: Wojciech Charasiński
"""

#%% Zadanie 1. lab2
"""Przy pomocy biblioteki random wygeneruj tablic¦ o rozmiarze podanym przez u»yt-
kownika. Tablica powinna zawiera¢ tylko zmienne typu oat. Nast¦pnie wyznacz

±redni¡ tablicy korzystaj¡c z metody wbudowanej, a nast¦pnie t¦ sam¡ ±redni¡ bez
metod wbudowanych. Wyznacz te» median¦ listy (skorzystaj z metody sort, ale nie
u»ywaj funkcji dotycz¡cej wyznaczania mediany)."""

import random as rnd
import statistics as stat

def losowa_tablica():
    rozmiar = int(input("Podaj rozmiar tablicy: \n"))
    tablica = []
    for _ in range(rozmiar):
        tablica.append(rnd.uniform(0, 100))

    print(tablica)
    print(f"Średnia wyliczona metodą wbudowaną: {stat.mean(tablica)}")
    print(f"Średnia wyliczona \"na piechotę\": {sum(tablica)/rozmiar}")
    print(f"Mediana wyliczona metodą wbudowaną: {stat.median(tablica)}")
    tablica.sort()
    indeks1 = (rozmiar - 1) // 2
    indeks2 = (rozmiar - 1) // 2 + 1
    if rozmiar % 2 == 0:
        mediana = (tablica[indeks2] + tablica[indeks1]) / 2
    else:
        mediana = tablica[indeks1]
    print(f"Mediana wyliczona \"na piechotę\": {mediana}")
    
losowa_tablica()

#%%  Zadanie 2. lab2
"""Wygeneruj losow¡ list¦ o wielko±ci zadanej przez u»ytkownika. Lista mo»e zawiera¢
aa«cuchy, zmienne typu oat, int oraz warto±ci boolowskie. Nast¦pnie napisz metod¦,
która przyjmuje tak¡ list¦ jako parametr i dzieli j¡ na 4 nowe listy zawieraj¡ce osobno
elementy string, oat, int oraz boolean."""


#%% Zadanie 3. lab2
"""Napisz funkcj¦ wypisuj¡c¡ co drugi element listy w odwrotnej kolejno±ci. Mo»na
u»y¢ metod wbudowanych dla list."""


#%% Zadanie 4. lab2
"""Dane s¡ dwie listy. Napisz metod¦ Merge, która poa¡czy listy tak, »eby elementy
pojawiaay si¦ na zmian¦."""


#%% Zadanie 5. lab2
"""Napisz waasn¡ metod¦ sort() umo»liwiaj¡c¡ sortowanie listy tak»e w sytuacji, kiedy
na li±cie znajduj¡ si¦ liczby i aa«cuchy. Zakaadamy, »e wszystkie elementy liczbowe
znajduj¡ si¦ na pocz¡tku, a aa«cuchy znajduj¡ si¦ w dalszej cz¦±ci listy - posortowane
saownikowo."""