# Comprehensions
## List-comprehension
Es kommt häufig vor, dass wir einfach eine Liste, oder ein Dictionary mit der Hilfe einer schon existierende Sequence definieren wollen. Wir können auch so vorgehen:
```
new_list = []
for element in sequence:
    if bedingung:
        new_list.append(change(element))
        # entspricht new_list += [change(element)]
```
Aber das ist schon 4 Zeilen Code! Können wir diese Liste irgendwie nicht so definieren, wie die Mathematiker?\
z.B. `{x/2 | x ∈ [-5, 1000) und x^2 < 1000}`? Das wäre ja ziemlich elegant.
Aber genau das machen Comprehensions. Erst mal gucken wir, wie man das hier ohne List-comprehension machen würde:
```
new_list = []
for x in range(-5, 1000): # range ist exklusiv
    if x**2 < 1000:
        new_list.append(x/2)
```
Das können wir jetzt als eine List-comprehension schreiben:\
`M = [x/2 for x in range(-5, 1000) if x**2 < 1000]`\
Das ist doch schön, ne?:) Sieht sehr ähnlich zur mathematischen Definition aus.\
Also, das Muster für ein List-comprehension ist folgendes: `list_comp = [change(element) for element in sequence if bedingung]`
> Man kann auch mehrere for-Schleifen benutzen: `list_comp = [change(e1, e2, ...) for e1 in seq1 if bed1 for e2 in seq2 if bed2 ...]`\
> Dabei ist die **Reihenfolge** der Schleifen **wichtig**!

### A1
Erstell die Folgende Listen mit List-comprehensions unter den Namen:
- `mul_3`: `[3, 6, 9, 12, 15, 18, 21]`
- `pot_3`: `[1, 3, 9, 27, 81, 243]`
- `abc`: alle die Kleinbuchstaben in einer Liste (benutze `chr(nummer)` und die Ascii-tabelle!)
- `ABC`: alle die Großbuchstaben
- `mul_3_doppelt_ungerade`: das doppelte der ungeraden Elementen der Liste `3_mul`.

### A2
Erstell die Folgende "multidimensionale" Listen mit List-comprehensions unter den Namen:
- `listen`: `[[], [], [], [], []]`
- `armband`: `[[8], [8], [8], [8], [8]]`
- `tictactoe`: `[['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]`\
Vorsicht, `['.', '.', '.']` sollst du auch mit einer List-comprehension machen!
- `telephone`: `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` (die innere Listen auch mit List-comp.!)

### A3

- Mache eine eindimensionale Liste aus der Liste `telephone`! (Ergebnis soll: `[1, 2, 3, 4, 5, 6, 7, 8, 9]` sein)
- Mache eine eindimensionale Liste aus der Liste `telephone`, mit umgedrehten Zeilen-reihenfolge! (Ergebnis soll: `[7, 8, 9, 4, 5, 6, 1, 2, 3]` sein)
- Mache eine eindimensionale Liste aus der Liste `telephone`, mit umgedrehten Spalten-reihenfolge! (Ergebnis soll: `[3, 2, 1, 6, 5, 4, 9, 8, 7]` sein)

## Generatoren
Du kennst schon Funktionen und return. Wenn du statt return, `yield` scheibst, BAMM, you've got a generator (auch Iterator genannt)!\
Der Unterschied: Wenn du eine _normale Funktion_ aufrufst, sie arbeitet bis sie zum return ankommt, dann gibt sie das zurück, was nach dem return steht, und das war's. Wenn du sie _nochmal_ aufrufst, fängt sie wieder **am Anfang** an.\
Ein Generator macht _erst mal_ quasi das selbe: er arbeitet bis er zum `yield` ankommt, dann gibt er das zurück, was danach steht. Aber wenn du ihn nochmal aufrufst, fängt er da an, wo er letztens aufgehört hat: nach dem `yield`, und geht weiter.
Man bekommt die yield-Werte auch ein bisschen anders: man muss next() auf dem Generator aufrufen, um das nächste Element zu erhalten. Oder eben mit einer for-Schleife durchiterieren.
```
def gen(n: int):
    yield "Round 1"
    # stop, und dann von hier geht's weiter
    yield "Round 2"
    # ende
    print("Ende. Du hast mir eine Zahl gegeben, ich gebe es zurück, hier:", n)
    
g = gen(6)
print(next(g))
print(next(g))
try:
    print(next(g))
except StopIteration:
    print("Ende!")

for round in gen(6):
    print(round)
```

### A4
- Erstell eine Generator-funktion mit einem Argument `n`, die mit jedem yield die n-fache der Zahlen von 1 bis 20 zurückgibt! (also wenn n=3, dann 3, 6, 9, ...)
- Erstell eine Generator-funktion mit einem Argument `n`, die mit jedem yield die n-te Potenz der Zahlen 1-20 zurückgibt! (n=3 => 1, 8, 27, 64, ...)

### A5
Erstell eine Generator-funktion mit einem Argument `n`, die die rekursive `fakul` Funktion aus dem ersten Blatt benutzt, um alle Fakultäten von 1 bis n zu yielden! (also sie soll 1!, 2!, 3!, ... yielden)

## Generator-comprehension
Eine Kombination aus comprehensions und Generatoren. _Die Schreibweise_ unterschiedet sich nur an den Klammern: **bei Generator-comprehensions benutzen wir runde Klammern** (also es gibt nichts wie Tuple-comprehensions)
Muster: `gen_comp = (change(element) for element in sequence if bedingung)`
> Natürlich sind hier auch mehrere for-Schleifen erlaubt.\
Verwendung von Generator-comprehensions ist das selbe, wie beim Generatoren:
```
g = (2**n for n in [4, 5, 6] if n%2==0)
print(next(g))
print(next(g))
try:
    print(next(g))
except StopIteration:
    print("Ende!")

for round in (2**n for n in [4, 5, 6] if n%2==0):
    print(round)
```

### A6
- Erstelle die entsprechende Generator-comprehensions für die Generatoren in A4 und A5!
- Erstelle einen Generator-comprehension, was dir die Zeilen vom List `telephone` (Aus A2) zurück gibt!

# Dictionaries
## Was sind sie?
Wir kennen schon Listen und Tuples alle. Listen sind veränderlich, Tuples nicht.
Listen und Tuples enthalten einfach mehrere einzelne Elemente.
Es kommt aber häufig vor, dass bestimmte Daten eine Beziehung zu anderen Daten haben.\
Wir haben z.B. eine Liste von Namen: `names = ['Coraline', 'Uwe', 'Fritz']`\
und eine Liste, was den Alter dieser Personen enthält: `ages = [16, 68, 32]`\
Das ist aber doch nicht wirklich nützlich. Wir wissen zwar, dass Coraline die erste Element in der Liste `names` ist,
deshalb gehört zu ihr das erste Element in der Liste `ages`, so hat Coraline der Alter von 16.
Wir haben aber keine direkte Verbindung zwischen Coraline und 16, und es ist auch nicht anschaulich.\
Aber genau dafür sind Dictionaries da!\
Dictionary ist der nützlichste Datenstruktur, wenn wir Dinge miteinander verknüpfen / zueinander zuordnen wollen.\
Der obige Beispiel mit einem Dict: `ages_of_people = {'Coraline': 16, 'Uwe': 68, 'Fritz': 32}`\
Die Verbindung ist sofort sichtbar.\
Wie du sehen kannst, es folgt folgendes Muster: `dict = {key: value, key: value, ...}`\
"key" und "value", weil das _key_ ist der _Schlüssel_, mit dem du zum _value_ zugreifen kannst, durch indexieren: `ages_of_people['Uwe']` entspricht `68`.
Du kannst auch alle keys und alle values eines Dictionary angucken: `ages_of_people.keys()` und `ages_of_people.values()` sind sogenannten View-Objekte (also _keine_ Listen, sondern eigentlich Generatoren), die mit dem Dictionary "synchronisiert" sind: wenn der Dictionary sich verändert, verändern sich diese View-Objekte auch.\
Deshalb muss man sie erst zu einer Liste convertieren (`list(ages_of_people.keys())` und `list(ages_of_people.values())`), wenn man sie als eine Liste benutzen möchte.\
Ansonst kann man durch diese Views ruhig durchiterieren:
```
for key in ages_of_people.keys():
    print(key)

# Anmerkung: man kann hier einfach "for key in ages_of_people" schreiben, in dieser Situation entspricht "ages_of_people" die keys von ages_of_people.
# Genauso mit dem convertieren: list(ages_of_people) == list(ages_of_people.keys())
for key in ages_of_people:
    print(key)
 
for value in ages_of_people.values():
    print(value)
```
Wenn man die keys und values beide erhalten möchte, schreibt man `ages_of_people.items()`. Dies ist eine **Liste** von Tuples: `[(key, value), (key, value), ...]`
Man kann das auch sehr schön durchiterieren:
```
for item in ages_of_people.items():
    print(item)
    print(item[0], item[1])
    
# da item hier ein tuple ist, können wir tuple-unpacking machen:
for (key, value) in ages_of_people.items(): # die Klammern um (key, value) kann man weglassen, aber erst mal ist es empfehlenswert, immer die Klammer hinzuschreiben
    print(key, value)
```

## A7
- Erstelle ein Dictionary `farbe` mit Sachen als keys (was du möchtest) und die Farben der Sachen als values. Es sollen dabei mehrere Sachen mit der gleichen Farbe geben!
- Print alle keys von `farbe`!
- Print alle values von `farbe`!
- Print alle key-value Paare von `farbe`!

## A8

# Dict-comprehension

# Trie
Dictionaries sind auch ideal für einfachere tree Strukturen, wie z.B. die sogenannte "trie" Struktur, womit man eine effizient suchbare Wörterbuch modellieren kann:
```
words = {'A': {'b': {'o': {0: 0},
                      'i': {0: 0,
                            't': {'u': {'r': {0: 0}}}
                           }
                     },
                'p': {'f': {'e': {'l': {0: 0}}}}
               }
         }
```
Dies ist verschachtelt: Dictionaries in dictionaries. Die `0: 0` Werte stehen für das Ende eines Wortes. Wie du sehen kannst, `Abi` und `Abitur` sind beide Wörter, beginnen aber mit den gleichen Buchstaben. Deshalb packen wir ein `0: 0` in den Dictionary von `i` rein, um anzuzeigen, dass dies das Ende eines sinnvollen Wortes ist.\
Wenn man es indexiert:
- `words['A']` bedeutet folgenden Dict:\
`{'b': {'o': {0: 0}, 'i': {0: 0, 't': {'u': {'r': {0: 0}}}}}, 'p': {'f': {'e': {'l': {0: 0}}}}}` Das kann man weiter indexieren!
- `words['A']['b']` bedeutet folgenden Dict:\
`{'o': {0: 0}, 'i': {0: 0, 't': {'u': {'r': {0: 0}}}}}`...
- `words['A']['b']['i']` bedeutet folgenden Dict:\
`{0: 0, 't': {'u': {'r': {0: 0}}}}` etc.

Ihr könnt sehen:
`words['A']['b']['o']` ist gerade `0: 0`, `words['A']['b']['i']`, `words['A']['b']['i']['t']['u']['r']` und `words['A']['p']['f']['e']['l']` auch.
