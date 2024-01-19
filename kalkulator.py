#!/usr/bin/env python3
def kalkulator():
print("Kalkulator podstaowywch operacji arytmetycznych")
def dodawanie(x,y):
return x+y
def odejmowanie(x, y):
return x-y
def mnozenie(x, y):
return x*y
def dzielenie(x, y):
return x/y
while True:
operacja = input("wybierz dzialanie :(+, -, *, /) lub 'q' by zakonczyc dzialanie)")
if operacja == 'q':
print("koniec pracy, zamkniecie kalkulatora")
break
liczba1 = double(input("podaj pierwsza liczbe"))
liczba2 = double(input("podaj druga liczbe"))
if operacja == '+':
print("WYNIK OPERACJI", dodawanie(liczba1, liczba2))
elif operacja == '-':
print("WYNIK OPERACJI", odejmowanie(liczba1, liczba2))
elif operacja == '*':
print("WYNIK OPERACJI", mnozenie(liczba1, liczba2))
elif operacja == '/':
print("WYNIK OPERACJI", dzielenie(liczba1, liczba2))
else
print("niedozwolona operacja")
kalkulator()
