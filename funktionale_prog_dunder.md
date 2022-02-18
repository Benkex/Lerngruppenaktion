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

Fachbegriffe:
- einstellige Funktion: Funktion mit einem Argument (meistens `n`)
- zweistellige Funktion: Funktion mit zwei Argumenten (meistens `x` und `y`; oder `a` und `b`)
- ...

### A1
- Erstell die einstellige lambda-Funktion `hoch2`, die `n^2` zurück gibt!
- Erstell die zweistellige lambda-Funktion `potenz`, die `x^y` zurück gibt!
- Erstell die zweistellige lambda-Funktion `add_operation`, die `a + b` zurück gibt!

### A
- Erstell die einstellige lambda-Funktion `mittelwert`, die eine Liste von integers nimmt (darfst du voraussetzen), und den Mittelwert von denen zurück gibt! Welche eingebaute Funktion ist uns dabei besonders nützlich?
- Erstell die einstellige lambda-Funktion `teiler`, die alle Teiler von `n` zurück gibt!
- Erstell die zweistellige lambda-Funktion `gem_teiler`, die die gemeinsame Teiler von `a` und `b` in einer Liste zurück gibt!
- Erstell die zweistellige lambda-Funktion `tuplize`, die `(a, b)` zurück gibt!
- Erstell die zweistellige lambda-Funktion `kreuz`, die zwei Listen nimmt, und die Kreuzprodukt von denen zurück gibt!\
Beispiel: für `a = [1, 2, 3], b = ['x', 'y']` ist `kreuz(a, b) == [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y'), (3, 'x'), (3, 'y')]`

### A
- Erstell die zweistellige lambda-Funktion `nebenklasse`, die ein integer `v` und eine Liste von integers `U` nimmt,
und eine Liste zurück gibt, in der du alle Elemente aus `U` zu `v` addierst!

### A
- Erstell die einstellige _rekursive_ lambda Funktion `sum_up`, die die Zahlen zwischen 1 und n summiert!
Du darfst dabei schon die name der Funktion verwenden: `sum_um = lambda ...: ... sum_up(...) ...`
Und diese Ausdruck: `(wert_wenn_true if bedingung else wert_wenn_false)` zum Stoppen.
- Erstell die einstellige _rekursive_ lambda-Funktion `fakultaet`, die die Fakultät von `n` zurück gibt!

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
> Gehen Sie dabei wie folgt vor:\
(a) Definieren Sie die folgenden Funktionen:\
– celsius_to_fahrenheit\
– fahrenheit_to_celsius\
– celsius_to_kelvin\
– kelvin_to_celsius\
Die Funktionen sollen die Temperatur als Argument vom Typ float entgegen nehmen und die entsprechend konvertierte Temperatur als Wert vom Typ
float zurückgeben.
Wie in der vorherigen Aufgabe, sollen diese Funktionen keine Side-Effects haben.
Beispielaufruf:
```
>>> celsius_to_fahrenheit(42.0)
107.6
```
> (b) (2 Punkte) Definieren Sie die Funktionen\
> – fahrenheit_to_kelvin\
> – kelvin_to_fahrenheit\
> Rufen Sie hierzu mehrere Funktionen aus dem vorherigen Aufgabenteil auf,
> anstatt die mathematischen Formeln zur Konvertierung direkt zu verwenden

Speichere die erstellte converter-Funktionen (celsius_to_fahrenheit, celsius_to_kelvin, ...) in einem Dictionary `convert`!\
Seien dabei die keys von `convert` die drei Maßeinheiten, die values wieder 3 Dictionaries,\
je mit 2 items, die als key die andere zwei Maßeinheiten haben, und als value die entsprechende converter-Funktion!\
Beispiel: `convert['C']['K'] == celsius_to_kelvin`\
Mit `convert` kannst du jetzt die Aufgabenteil (c) sehr einfach und elegant lösen, vor allem OHNE if-Verzweigungen!
> (c) Verwenden Sie ~~die Funktionen aus den vorherigen Aufgabenteilen~~~ die Funktion `convert` zusammen mit input und print ~~und if-Verzweigungen~~,
> um das gewünschte Verhalten zu erzeugen (wie im Einleitungstext der Aufgabe beschrieben).
