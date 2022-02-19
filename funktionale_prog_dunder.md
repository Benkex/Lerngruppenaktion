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
- Erstell die einstellige lambda-Funktion `hoch2`, die die zweite Potenz des Arguments zurück gibt!
- Erstell die zweistellige lambda-Funktion `potenz`, die die `y`-te Potenz von `x` zurück gibt! (`potenz(2, 3) == 8`)
- Erstell die zweistellige lambda-Funktion `add_operation`, die die Argumente zusammenaddiert!

### A2
- Erstell die einstellige lambda-Funktion `mittelwert`, die eine Liste von integers nimmt (darfst du voraussetzen), und den Mittelwert von denen zurück gibt! Welche eingebaute Funktion ist uns dabei besonders nützlich?
- Erstell die einstellige lambda-Funktion `teiler`, die alle positive Teiler von `n` in einer Liste zurück gibt!
    - `teiler(36) = [1, 2, 3, 4, 6, 9, 12, 18, 36]`,
    - `teiler(0) = []`
    - `teiler(-3) = [1, 3]`
- Erstell die zweistellige lambda-Funktion `gem_teiler`, die die gemeinsame positive Teiler von `x` und `y` in einer Liste zurück gibt!
    - `gem_teiler(12, 81) == [1, 3]`
    - `gem_teiler(12, 23) == [1]`
    - `gem_teiler(-5, 15) == [1, 5]`
- Erstell die zweistellige lambda-Funktion `tuplize`, die `(x, y)` zurück gibt!
- Erstell die zweistellige lambda-Funktion `kreuz`, die zwei Listen nimmt, und die Kreuzprodukt von denen zurück gibt!
    - Für `num = [1, 2, 3], let = ['x', 'y']` ist `kreuz(num, let) == [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y'), (3, 'x'), (3, 'y')]`

### A3
- Erstell die zweistellige lambda-Funktion `nebenklasse`, die ein integer `v` und ein Sequence von integers `U` nimmt,
und ein **set** zurück gibt, in der du alle Elemente aus `U` zu `v` addierst! Verwende dabei die vorher definierte `add_operation`!\
Ein set-comprehension macht man wie üblich, aber mit geschwungene Klammern: `{change(item) for item in seq if bedingung}`\
Wir benutzen set, weil dann sich keine Elemente wiederholen werden. Eine Nebenklasse ist eine Menge, und in einer Menge darf sich kein Element wiederholen.\
(Geholt aus LA Vorlesung)
    - `nebenklasse(3, [-8, 1, 5, -2, 0]) = {-5, 4, 8, 1, 3}`

### A4
- Erstell die einstellige _rekursive_ lambda Funktion `sum_up`, die die Zahlen zwischen 1 und n summiert!
Du darfst dabei schon die name der Funktion verwenden: `sum_um = lambda ...: ... sum_up(...) ...`\
Und diese Ausdruck: `(wert_wenn_true if bedingung else wert_wenn_false)` zum Stoppen.
    - `sum_up(100) == 5050`
- Erstell die einstellige _rekursive_ lambda-Funktion `fakultaet`, die die Fakultät von `n` zurück gibt!
- Erstell die einstellige _rekursive_ lambda-Funktion `fibo` zur Erstellung von Fibonacci-Reihen bis `n`!
    - Fibonacci-Reihe für n=2: `[0, 1]`
    - Fibonacci-Reihe für n=5: `[0, 1, 1, 2, 3]`
    - Fibonacci-Reihe für n=6: `[0, 1, 1, 2, 3, 5]`

### A5
(EidP Aufgabe 3.2)
https://proglang.informatik.uni-freiburg.de/teaching/info1/2021/exercise/sheet03.pdf \
Speichere die erstellte converter-Funktionen (celsius_to_fahrenheit, celsius_to_kelvin, ...) in einem Dictionary `convert`!\
Seien dabei die keys von `convert` die drei Maßeinheiten, die values wieder 3 Dictionaries,\
je mit 2 items, die als key die andere zwei Maßeinheiten haben, und als value die entsprechende converter-Funktion!\
Beispiel: `convert['C']['K'] == celsius_to_kelvin`\
Mit `convert` kannst du jetzt die Aufgabenteil (c) sehr einfach und elegant lösen, vor allem OHNE if-Verzweigungen!
> (c) Verwenden Sie ~~die Funktionen aus den vorherigen Aufgabenteilen~~ **die Struktur `convert`** zusammen mit input und print ~~und if-Verzweigungen~~,
> um das gewünschte Verhalten zu erzeugen (wie im Einleitungstext der Aufgabe beschrieben).


# Dunder Methoden
Klassen, die man selbst erstellt, können beliebig viele Eigenschaften und Methoden haben, um das gewünschte Verhalten zu erreichen.

Aber dennoch gibt es einige Funktionen und Operatoren in Python, die man nicht direkt über Methoden steuern kann. Was zum Beispiel ist `len(myObj)`? Um in diesen Fällen den Rückgabe-Wert zu bestimmen, kommen die Dunder Methoden zum Einsatz (in dem Fall `myObj.__len__()`).

> WICHTIG: \
Diese Dunder Methoden Sollten nie direkt aufgerufen werden, sondern werden vom Interpreter automatisch aufgerufen, wenn sie gebraucht werden.

Hier eine Übericht über die wichtigsten:

| Methoden-Name | Aufgerufen durch |
| ------------- | ------------- |
| `__post_init__(self)` | `myObj = myClass(args)`  |
| `__len__(self)` | `len(myObj)`  |
| `__str__(self)` | `str(myObj)`  |
| `__getitem__(self, index)` | `myObj[0]`  |
| Vorzeichen |  |
| `__pos__(self)` | `+myObj`  |
| `__neg__(self)` | `-myObj`  |
| Vergleiche |  |
| `__lt__(self, other)` | `myObj < other`  |
| `__eq__(self, other)` | `myObj == other`  |
| `__gt__(self, other)` | `myObj > other`  |
| Rechnen-Operatoren |  |
| `__add__(self, other)` | `myObj + other`  |
| `__sub__(self, other)` | `myObj - other`  |
| `__mul__(self, other)` | `myObj * other`  |
| `__div__(self, other)` | `myObj / other`  |
| Rechnen-Operatoren (rechts) |  |
| `__radd__(self, other)` | `other + myObj`  |
| `__rsub__(self, other)` | `other - myObj`  |
| `__rmul__(self, other)` | `other * myObj`  |
| `__rdiv__(self, other)` | `other / myObj`  |

> Die radd (Right-Add) usw. sind deswegen nötig weil Python als erstes den linken Term überprüft. Also bei `other + myObj` wird erst `other.__add__()` aufgerufen, die aber unsere Klasse wahrscheinlich nicht kennt. Wenn `other.__add__()` einen Fehler ausgibt, probiert Python einfach `myObj.__radd__()`.

### A6
Erstelle eine Datenklasse Color, die drei Eigenschaften red, green, blue besitzt. Die Werte dürfen dabei nur eine ganze Zahl zwischen 0 und 255 sein. \
Schreibe dazu noch eine Methode `__str__`, die die aktuellen Werte für red, green und blue ausgibt.
> Beispiel-Ausagbe: "Color with RGB = (255, 0, 255)"

### A7
Erstelle für die Klasse Color die Mehtode `add`. Diese Methode soll ein `other` Argument akzeptieren. Das Argument kann entweder eine andere Farbe oder eine ganze Zahl sein:
- Ist other eine Farbe, soll eine neue Farbe ausgegeben werden, dessen Farbwerte jeweils die Summen der anderen Farbwerte sind, aber 255 nicht überschreiten.
- Ist other eine ganze Zahl, soll jeder Farb-Wert um die Zahl erhöht werden (aber 255 nicht überschreitet).
- Ist other ein anderer Typ, soll ein Fehler ausgegeben werden.

> Statt die aktuelle Farbe zu verändern, soll immer eine neue Farbe erstellt werden

Verknüpfe die Methode `add` mit den Dunder-Methoden `__add__` und `__radd__`.

### A8
Erstelle eine Methode `get_brightness`, die die Helligkeit zurückgibt. Die Formel dazu ist `brightness = (0.2126*R + 0.7152*G + 0.0722*B)`.

Benutze diese Methode, um die Dunder Methoden `__lt__`, `__eq__` und `__gt__` zu schreiben, die die Helligkeit zweier Farben oder die Helligkeit mit einer Zahl vergleicht.

### A9
Erstelle die Dunder Methoden `__pos__` und `__neg__`, die die Farbe selber bzw. das Invertierte der Farbe zurückgeben. \
Die invertierte der Farbe kann man berechnen indem man bei jedem Farbwert den aktuellen Farbwert von 255 abzieht (`inverted = 255 - current`).

> Statt die aktuelle Farbe zu verändern, soll immer eine neue Farbe erstellt werden

### A10
Erstelle die Dunder Methode `__getitem__`, die als index einen String akzeptiert. Ist der String "red", "green" oder "blue" soll der entsprechende Farbwert zurückgegeben werden.

### A11
Erstelle eine methode `colorMap(f)` die als Argument f eine Funktion annimmt. Diese Funktion soll auf die eigenen red, green und blue Eigenschaften angewendet werden und aus den Rückgabewerten der Funktion eine neue Color Instanz erstellt werden.

Benutze diese `colorMap` Funktion um die Addition mit einer ganzen Zahl aus A7) und das Invertieren der Color in A9) mithilfe von funktionaler Programmierung zu lösen.
