# Dictionaries
## Was sind sie?
> Wir kennen schon Listen und Tuples alle. Listen sind veränderlich, Tuples nicht.
> Listen und Tuples enthalten einfach mehrere einzelne Elemente.
> Es kommt aber häufig vor, dass bestimmte Daten eine Beziehung zu anderen Daten haben.\
> Wir haben z.B. eine Liste von Namen: `names = ['Coraline', 'Uwe', 'Fritz']`\
> und eine Liste, was den Alter dieser Personen enthält: `ages = [16, 68, 32]`\
> Das ist aber doch nicht wirklich nützlich. Wir wissen zwar, dass Coraline die erste Element in der Liste `names` ist,
> deshalb gehört zu ihr das erste Element in der Liste `ages`, so hat Coraline der Alter von 16.
> Wir haben aber keine direkte Verbindung zwischen Coraline und 16, und es ist auch nicht anschaulich.\
> Aber genau dafür sind Dictionaries da!\
> Dictionary ist der nützlichste Datenstruktur, wenn wir Dinge miteinander verknüpfen / zueinander zuordnen wollen.\
> Der obige Beispiel mit einem Dict: `ages_of_people = {'Coraline': 16, 'Uwe': 68, 'Fritz': 32}`\
> Die Verbindung ist sofort sichtbar.

## A1
Erstelle ein Dictionary mit 

# Trie
Dictionaries sind auch ideal für einfachere tree Strukturen, wie z.B. die sogenannte "trie" Struktur, womit man eine effizient suchbare Wörterbuch modellieren kann:\
`words = {'A': {'b': {'o': {0: 0},
                      'i': {0: 0,
                            't': {'u': {'r': {0: 0}}}
                           }
                     },
                'p': {'f': {'e': {'l': {0: 0}}}}
               }
         }`
Dies ist verschachtelt: Dictionaries in dictionaries. Die `0: 0` Werte stehen für das Ende eines Wortes. Wie du sehen kannst, `Abi` und `Abitur` sind beide Wörter, beginnen aber mit den gleichen Buchstaben. Deshalb packen wir ein `0: 0` in den Dictionary von `i` rein, um anzuzeigen, dass dies das Ende eines sinnvollen Wortes ist.\
Wenn man es indexiert:
- `words['A']` bedeutet folgenden Dict: `{'b': {'o': {0: 0}, 'i': {0: 0, 't': {'u': {'r': {0: 0}}}}}, 'p': {'f': {'e': {'l': {0: 0}}}}}` Das kann man weiter indexieren!
- `words['A']['b']` bedeutet folgenden Dict: `{'o': {0: 0}, 'i': {0: 0, 't': {'u': {'r': {0: 0}}}}}`...
- `words['A']['b']['i']` bedeutet folgenden Dict: `{0: 0, 't': {'u': {'r': {0: 0}}}}` etc.

Ihr könnt sehen:
`words['A']['b']['o']` ist gerade `0: 0`, `words['A']['b']['i']`, `words['A']['b']['i']['t']['u']['r']` und `words['A']['p']['f']['e']['l']` auch.

# Comprehensions
## Einleitung
> Es kommt häufig vor, dass wir einfach eine Liste, oder ein Dictionary mit der Hilfe einer schon existierende Sequence definieren wollen. Wir können auch so vorgehen:
> `new_list = []
> for element in sequence:
>     if bedingung:
>         new_list.append(element)
>         # entspricht new_list += [element]`
> Aber das ist schon 4 Zeilen Code! Können wir diese Liste irgendwie nicht so definieren, wie die Mathematiker? z.B. `{x ∈ [-5, 1000) | x^2 < 1000}`? Das wäre ja ziemlich elegant.
> Aber genau das machen Comprehensions. Ein direkter Vergleich mit list-comprehension und mathematische Mengen: \
`M = {x ∈ [-5, 1000)             |  x^2 < 1000}`\
`M = [x for x in range(-5, 1000) if x**2 < 1000]`\
> Das ist doch schön, ne?:)\
> Dict-comprehension ist nur 
