# Funktionale Programmierung
## lambda
Das Besondere bei der funktionale Programmierung ist, dass sie Funktionen als Objekten behandelt:
Funktionen dürfen als Funktionargumente angegeben werden, in Listen gespeichert werden und als Listenelemente aufgerufen werden, etc.
Die allerwichtigste Struktur dabei ist `lambda`.
Die Syntax einer Funktion, die etwas sofort zurück gibt...
```
def func(arg1, arg2, ..., argN):
    return statement(arg1, arg2, ..., argN)
```
...kann jetzt einfacher als ein selbstständiger Objekt geschrieben werden: \
`func = lambda arg1, arg2, ..., argN: statement(arg1, arg2, ..., argN)`

### A1
- Erstell eine einstellige lambda-Funktion (d.h. sie soll ein Argument haben, `n` z.B.), die n^2 zurück gibt!
- Erstell eine einstellige lambda-Funktion mit Argument `n`, die 


### A
(EidP Aufgabe 3.2)
> In dieser Aufgabe sollen Sie ein Programm schreiben, welches eine Temperatur in
> Celsius (C), Fahrenheit (F) oder Kelvin (K) entgegen nimmt und diese zu einer anderen Temperatureinheit konvertiert und ausgibt.
> Ruft man das Programm auf, um 42 Grad Celsius nach Kelvin zu konvertieren,
> soll dabei exakt die folgende Ein- und Ausgabe erscheinen (Benutzereingaben in blau hervorgehoben):
```
$ python3 temperature.py
Enter source unit [C / F / K]: C
Enter source value: 42.0
Enter target unit [C / F / K]: K
42.0 C corresponds to 315.15 K
```
> Gehen Sie dabei wie folgt vor:
(a) Definieren Sie die folgenden Funktionen:
– celsius_to_fahrenheit
– fahrenheit_to_celsius
– celsius_to_kelvin
– kelvin_to_celsius
Die Funktionen sollen die Temperatur als Argument vom Typ float entgegen nehmen und die entsprechend konvertierte Temperatur als Wert vom Typ
float zurückgeben.
Wie in der vorherigen Aufgabe, sollen diese Funktionen keine Side-Effects haben.
Beispielaufruf:
```
>>> celsius_to_fahrenheit(42.0)
107.6
```
> (b) (2 Punkte) Definieren Sie die Funktionen
> – fahrenheit_to_kelvin
> – kelvin_to_fahrenheit
> Rufen Sie hierzu mehrere Funktionen aus dem vorherigen Aufgabenteil auf,
> anstatt die mathematischen Formeln zur Konvertierung direkt zu verwenden

Speichere die erstellte converter-Funktionen (celsius_to_fahrenheit, celsius_to_kelvin, ...) in einem Dictionary `convert`!
Seien dabei die keys von `convert` die drei Maßeinheiten, die values wieder 3 Dictionaries,
je mit 2 items, die als key die andere zwei Maßeinheiten haben, und als value die entsprechende converter-Funktion!
Beispiel: `convert['C']['K'] == celsius_to_kelvin`
Mit `convert` kannst du jetzt die Aufgabenteil (c) sehr einfach und elegant lösen, vor allem OHNE if-Verzweigungen!
> (c) Verwenden Sie die Funktionen aus den vorherigen Aufgabenteilen zusammen mit input, print ~~und if-Verzweigungen~~,
> um das gewünschte Verhalten zu erzeugen (wie im Einleitungstext der Aufgabe beschrieben).
