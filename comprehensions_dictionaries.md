# Comprehensions
## List-comprehension
Es kommt häufig vor, dass wir einfach eine Liste, oder einen Dictionary mit der Hilfe einem schon existierenden Sequence definieren wollen.
Wir können auch so vorgehen:
```py
new_list = []
for element in sequence:
    if bedingung(element):
        new_list.append(change(element)) # entspricht new_list += [change(element)]
```
Aber das ist schon 4 Zeilen Code! Können wir diese Liste irgendwie nicht so definieren, wie die Mathematiker?\
Also wie `L = {C(x) | x ∈ M und B(x)}`, wobei C(x) eine Funktion ist, die x verwandelt, und B(x) ist eine Bedingung über x, die entweder wahr oder falsch ist.\
z.B. `{x/2 | x ∈ [-5, 1000) und x^2 < 1000}`\
Aber genau das machen Comprehensions. Erst mal gucken wir, wie man das hier ohne List-comprehension machen würde:
```py
new_list = []
for x in range(-5, 1000): # range ist exklusiv
    if x**2 < 1000:
        new_list.append(x/2)
```
Das können wir jetzt als eine List-comprehension schreiben:\
`M = [x/2 for x in range(-5, 1000) if x**2 < 1000]`\
Das ist doch schön, oder?:) Sieht sehr ähnlich zur mathematischen Definition aus.\
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
Du kennst schon Funktionen und **return**. Wenn du statt return, `yield` schreibst, BAMM, you've got a generator (auch Iterator genannt)!\
Der Unterschied: Wenn du eine _normale Funktion_ aufrufst, sie arbeitet bis sie zum return ankommt, dann gibt sie das zurück, was nach dem return steht, und das war's. Wenn du sie _nochmal_ aufrufst, fängt sie wieder **am Anfang** an.\
Ein Generator macht _erst mal_ quasi das selbe: er arbeitet bis er zum `yield` ankommt, dann gibt er das zurück, was danach steht. Aber wenn du ihn nochmal aufrufst, fängt er da an, wo er letztens aufgehört hat: nach dem `yield`, und geht weiter.
Man bekommt die yield-Werte auch ein bisschen anders: man muss next() auf dem Generator aufrufen, um das nächste Element zu erhalten. Oder eben mit einer for-Schleife durchiterieren.
```py
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
Eine Kombination aus comprehensions und Generatoren. _Die Schreibweise_ unterschiedet sich nur an den Klammern:\
**bei Generator-comprehensions benutzen wir runde Klammern** (also es gibt keinen Tuple-comprehensions!)\
Muster: `gen_comp = (change(element) for element in sequence if bedingung)`
> Natürlich sind hier auch mehrere for-Schleifen erlaubt.

Verwendung von Generator-comprehensions ist das selbe, wie beim Generatoren:
```py
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
```py
for key in ages_of_people.keys():
    print(key)

# Anmerkung: man kann hier einfach "for key in ages_of_people" schreiben,
#   "ages_of_people" entspricht hier die keys von ages_of_people (ages_of_people.keys()).
# Genauso mit dem convertieren: list(ages_of_people) == list(ages_of_people.keys())
for key in ages_of_people:
    print(key)
 
for value in ages_of_people.values():
    print(value)
```
Wenn man die keys und values beide erhalten möchte, schreibt man `ages_of_people.items()`. Dies ist eine **Liste** von Tuples: `[(key, value), (key, value), ...]`
Man kann das auch sehr schön durchiterieren:
```py
for item in ages_of_people.items():
    print(item)
    print(item[0], item[1])
    
# da item hier ein tuple ist, können wir tuple-unpacking machen:
for (key, value) in ages_of_people.items(): # die Klammern um (key, value) kann man weglassen,
    print(key, value)                       # aber erst mal ist es empfehlenswert, immer die Klammer hinzuschreiben
```

## A7
- Erstelle einen Dictionary `farbe` mit Sachen als keys (was du möchtest) und die Farben der Sachen als values. Es sollen dabei mehrere Sachen mit der gleichen Farbe geben!
- Print alle keys von `farbe`!
- Print alle values von `farbe`!
- Print alle key-value Paare von `farbe`!

## A8
Fasse jetzt den Dictionary `farbe` zu einem anderen Dictionary (`farbe_anzahl`) zusammen, der die Farben als keys, und Anzahl der Sachen mit dieser Farbe als values hat!
Es soll am Ende z.B. so aussehen: `{'Farbe1': 3, 'Farbe2': 1, 'Farbe3': 4}`

# Dict-comprehension
Dict-comprehension geht gleich so, wie List-comprehension, nur ist es halt ein Dictionary.
Beispiel: `f_x_hoch_2 = {x: pow(x, 2) for x in range(100)}

## A9
Erstelle einen Dictionary `str_int` *mit Dict-comprehension*, der zufällige strings der Länge 4 als keys, und zufällige Zahlen als values hat!
- `str_int` soll 8 Items haben!
- Benutze dabei `chr(num)`, str * int Multiplikation und `random.randint(start, end)`!

## A10
Erstelle einen Dict `str_float` *mit Dict-comprehension*, der das gleiche ist, wie `str_int`, nur sollen die Values jetzt floats sein.
- Benutze dabei `float(num)` und `str_int.items()`!

## A11
Erstelle einen Dict `str_double` *mit Dict-comprehension*, der das gleiche ist, wie `str_float`, nur sollen die Values jetzt mit 2 multipliziert werden.
- Benutze dabei `str_int.keys()`, `str_int.values()` und `zip(seq1, seq2)`!

---

---

# -------------- Trie ----------------
Dictionaries sind auch ideal für einfachere tree Strukturen, wie z.B. die sogenannte *trie*-Struktur, womit man eine effizient suchbare Wörterbuch modellieren kann.  
Um das verstehen zu können, gucken wir erst verschachtelte Dictionaries an.  
Betrache folgendes Beispiel:  
1. Sechs Schüler (Anna, Bella, Chris, Dennis, Egor und Fabian) haben Präsentationen in verschiedenen Fächern gemacht.
    - Zum Beispiel (Bella und Chris in Mathe), (Egor in Physik), (Dennis, Anna und Fabian in Chemie).
    - Wir speichern jetzt die Anzahl der Leute, die den gleichen Fach gewählt haben.  
    Wir wollen also so was erreichen: `print(anzahl_leute_in['Fach'])` printet die Anzahl der Leute, die ihre Präsi im Fach "Fach" gemacht haben.
    - Dafür brauchen wir einen Dictionary, und wir definieren es auf die folgende Weise:
    ```py
    anzahl_leute_in = {'Mathe': 2, 'Physik': 1, 'Chemie': 3}
    ```
    - Dabei können wir dann zum Anzahl durch Indexieren zugreifen:  
    `print(anzahl_leute_in['Chemie'])` wird eben `3` ausprinten,  
    `print(anzahl_leute_in['Mathe'])` wird `2` ausprinten und  
    `print(anzahl_leute_in['Physik'])` wird `1` ausprinten.
2. Die Schüler haben aber auch Noten bekommen, so sieht es aus:  

    | Fach   | Person | Note |
    | ------ | ------ | ---- |
    | Mathe  | Bella  | 1.3  |
    | Mathe  | Chris  | 2.0  |
    | Physik | Egor   | 1.0  |
    | Chemie | Dennis | 2.7  |
    | Chemie | Anna   | 1.7  |
    | Chemie | Fabian | 2.0  |
  - Jetzt wollen wir gerne innerhalb eines Faches speichern, was für eine Note die Leute gekriegt haben.
  - Dafür machen wir erst mal 3 Dictionaries zu den drei Fächer, in dem wir die Leute mit ihren Noten "verbinden":
  ```py
  mathe_note_von = {'Bella': 1.3, 'Chris': 2.0}
  physik_note_von = {'Egor': 1.0}
  chemie_note_von = {'Dennis': 2.7, 'Anna': 1.7, 'Fabian': 2.0}
  # Sie könnten auch so aussehen:
  mathe_note_von = {
    'Bella': 1.3,
    'Chris': 2.0
  }
  # usw.
  # Die Definition hier ist identisch mit der vorigen Definition, sieht aber besser aus.
  ```
  - Also `print(mathe_note_von['Chris'])` printet jetzt `2.0`,  
    `print(chemie_note_von['Anna'])` printet `1.7` usw.
  - *Definieren wir* mal einen neuen (verschachtelten) Dict `note_von_fach_person`, die sich so verhält:  
    `print(note_von_fach_person['Fach']['Person'])` printet die Note des "Person"s in dem angegebenen "Fach".
  - Beispiel: `print(note_von_fach_person['Physik']['Egor'])` soll `1.0` printen.
  - Es bleibt nur noch ein Schritt übrig, um `note_von_fach_person` zu definieren.  
    **Versuche es erst mal selbst! Gucke nicht sofort in die Lösung!**  
    Kombiniere dein Wissen aus (1.) und (2.)!
  <details>
    <summary><strong>Lösung</strong></summary>  

    ```py
    note_von_fach_person = {'Mathe': mathe_note_von, 'Physik': physik_note_von, 'Chemie': chemie_note_von}
    # oder das geht auch:
    note_von_fach_person = {
        'Mathe': {'Bella': 1.3, 'Chris': 2.0},
        'Physik': {'Egor': 1.0},
        'Chemie': {'Dennis': 2.7, 'Anna': 1.7, 'Fabian': 2.0}
    }
    # oder halt...
    note_von_fach_person = {
        'Mathe': {
            'Bella': 1.3,
            'Chris': 2.0
        },
        'Physik': {
            'Egor': 1.0
        },
        'Chemie': {
            'Dennis': 2.7,
            'Anna': 1.7,
            'Fabian': 2.0
        }
    }
    ```
  </details>

Wenn du jetzt damit fertig bist, hast du einen verschachtelten Dictionary. Dicts in Dicts, das wird noch spannend:)  
Wir haben z.B. 4 Wörter: Apfel, Abo, Abi und Abitur. Die wollen wir jetzt in einer *trie*-Struktur speichern.  
Wenn wir eine *trie*-Struktur veranschaulichen, sieht es so aus:
```
     words
       |
       A
      / \
     b   p
    / \   \
   i   o   f
  / \   \   \
 t   0   0   e
 |           |
 u           l
 |           |
 r           0
 |
 0
```
Die implementierung geht so:

```py
words = {
    'A': {
        'p': {
            'f': {
                'e': {
                    'l': {0: 0}
                }
            }
        },
        'b': {
            'o': {0: 0},
            'i': {
                0: 0,
                't': {
                    'u': {
                       'r': {0: 0}
                    }
                }
            }
        }
    }
}
```
Dies ist jetzt verschachtelt: Dicts in Dicts, nur mit mehr "Levels" als das letze mal.  
Es ist eine *trie*-Struktur: es speichert Wörter in einem Baum-ähnlichen Form.  

Die `0: 0` Items in diesem Dict `words` stehen für das Ende eines sinnvollen Wortes. Wie du sehen kannst, `Abi` und `Abitur` sind beide sinnvolle Wörter, `Abi` ist aber in `Abitur` enthalten. Deshalb packen wir ein `0: 0` in den Dictionary von `i` rein, um anzuzeigen, dass dies das Ende eines sinnvollen Wortes ist.  
**So funktioniert es**, wenn man es indexiert:
- `words` ist so zu sagen der erste "layer".
- `words['A']` bedeutet folgenden Dict:  
`{'b': {'o': {0: 0}, 'i': {0: 0, 't': {'u': {'r': {0: 0}}}}}, 'p': {'f': {'e': {'l': {0: 0}}}}}`  
Dies ist der zweite "layer", der sub-Dict von `A`.
Das kann man aber ja weiter indexieren! Guck das z.B. an:  
{<span style="color: magenta">'b': </span><span style="color:red">{'o': {0: 0}, 'i': {0: 0, 't': {'u': {'r': {0: 0}}}}}</span>, 'p': {'f': {'e': {'l': {0: 0}}}}}  
`'b'` ist der Index für `{'o': {0: 0}, 'i': {0: 0, 't': {'u': {'r': {0: 0}}}}}`.
- `words['A']['b']` bedeutet `{'o': {0: 0}, 'i': {0: 0, 't': {'u': {'r': {0: 0}}}}}`... (dritte "layer", sub-Dict von `b`)
- `words['A']['b']['i']` bedeutet `{0: 0, 't': {'u': {'r': {0: 0}}}}` (vierte "layer", sub-Dict von `i`)  
Hier sieht man schon ein `0: 0` drinnen, also ist `Abi` ein sinnvolles Wort, usw.

Ihr könnt sehen:
- `0 in words['A']['b']['i'] == True`...............(das gleiche wie `0 in words['A']['b']['i'].keys() == True`, wie weiter oben erklärt)
- `0 in words['A']['b']['i']['t']['u']['r'] = True`
- `0 in words['A']['b']['o'] == True`
- `0 in words['A']['p']['f']['e']['l'] == True`

Aber
- `0 in words['A']['b']['i']['t'] == False`
- `0 in words['A']['p']['f']['e'] == False`

Das macht Sinn, da `'Abit'` und `'Apfe'` keine sinnvolle Wörter sind.  
Wir haben ja in dem entsprechenden Dict nur dann `0: 0` gespeichert, falls ein sinnvolles Wort an der stelle beendet hat.  

Ok, aber wozu das ganze? Die Sache ist:
- man kann in einer *trie*-Struktur wirklich wirklich **wirklich** schnell suchen, d.h. checken, ob eine Zeichenkette in `words` enthalten ist. Ich sage Zeichenkette, weil was wir suchen, kann auch `'Ahfdnfjaskfd'` sein, und das ist natürlich kein sinnvolles Wort, sondern nur eine Zeichenkette (`string`).

## A12
Erstelle Funktionen `insert_to(trie: dict, word: str)` und `search_in(trie: dict, word: str)`!
- `insert_into` soll den Argument `word` in die trie-Struktur reinnehmen. Die Funktion kann rekursiv sein, muss aber nicht. Es geht sogar einfacher ohne Rekursion.
  <details><summary>Hint</summary>
  Gehe Buchstabe nach Buchstabe. Erste Buchstabe von `wort` soll im ersten "layer" von trie sein, dann zweite Buchstabe im zweiten "layer" im entsprechenden sub-Dict, usw. Beispiel: `wort = "Birne"`. Dann checke ich, ob `B` im 1. layer von trie ist, wenn ja, gehe ich im sub-Dict von `B` rein, wenn nicht, füge ich `B` einfach rein mit einem leeren subdict, und gehe da rein.
  </details>
  <details><summary>Hint</summary>
  Checke die Buchstaben einzeln: ist die erste Buchstabe im ersten "layer" von trie? Wenn ja, muss ich in dem sub-Dict von diesem Buchstaben weiter suchen, wenn nicht, breche ab.
  </details>