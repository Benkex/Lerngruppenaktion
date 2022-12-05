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

### A1
Erstelle eine Datenklasse Color, die drei Eigenschaften red, green, blue besitzt. Die Werte dürfen dabei nur eine ganze Zahl zwischen 0 und 255 sein. \
Schreibe dazu noch eine Methode `__str__`, die die aktuellen Werte für red, green und blue ausgibt.
> Beispiel-Ausagbe: "Color with RGB = (255, 0, 255)"

### A2
Erstelle für die Klasse Color die Mehtode `add`. Diese Methode soll ein `other` Argument akzeptieren. Das Argument kann entweder eine andere Farbe oder eine ganze Zahl sein:
- Ist other eine Farbe, soll eine neue Farbe ausgegeben werden, dessen Farbwerte jeweils die Summen der anderen Farbwerte sind, aber 255 nicht überschreiten.
- Ist other eine ganze Zahl, soll jeder Farb-Wert um die Zahl erhöht werden (aber 255 nicht überschreitet).
- Ist other ein anderer Typ, soll ein Fehler ausgegeben werden.

> Statt die aktuelle Farbe zu verändern, soll immer eine neue Farbe erstellt werden

Verknüpfe die Methode `add` mit den Dunder-Methoden `__add__` und `__radd__`.

### A3
Erstelle eine Methode `get_brightness`, die die Helligkeit zurückgibt. Die Formel dazu ist `brightness = (0.2126*R + 0.7152*G + 0.0722*B)`.

Benutze diese Methode, um die Dunder Methoden `__lt__`, `__eq__` und `__gt__` zu schreiben, die die Helligkeit zweier Farben oder die Helligkeit mit einer Zahl vergleicht.

### A4
Erstelle die Dunder Methoden `__pos__` und `__neg__`, die die Farbe selber bzw. das Invertierte der Farbe zurückgeben. \
Die invertierte der Farbe kann man berechnen indem man bei jedem Farbwert den aktuellen Farbwert von 255 abzieht (`inverted = 255 - current`).

> Statt die aktuelle Farbe zu verändern, soll immer eine neue Farbe erstellt werden

### A5
Erstelle die Dunder Methode `__getitem__`, die als index einen String akzeptiert. Ist der String "red", "green" oder "blue" soll der entsprechende Farbwert zurückgegeben werden.

### A6
Erstelle eine methode `colorMap(f)` die als Argument f eine Funktion annimmt. Diese Funktion soll auf die eigenen red, green und blue Eigenschaften angewendet werden und aus den Rückgabewerten der Funktion eine neue Color Instanz erstellt werden.

Benutze diese `colorMap` Funktion um die Addition mit einer ganzen Zahl aus A7) und das Invertieren der Color in A9) mithilfe von funktionaler Programmierung zu lösen.
