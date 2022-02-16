### Bäume
> In den kommenden Aufgaben, wollen wir uns eine Übersicht über Bäume erschaffen.
> Dazu erstellen wir uns erst einen einfachen Binärbaum, und gehen später über zu allgemeinen Bäumen.
> Unterdessen schauen wir uns an wie man auf Bäumen arbeiten kann.
> Zur Unterstützung kann das in tree.py bereitgestellte Template verwendet werden.
> Dabei soll stetig auf richtiges Typing geachtet werden.

## A1
Ergänze die Datenklasse BinaryNode mit folgenden Instanzen:
- `id` welches eine ganze Zahl ist,
- `left` welches entweder einen Typ von `BinaryNode`, oder `None` hat (`"Optional[BinaryNode]"`), und
- `right` genauso, wie `left`.

## Kurz über Dundermethoden
> Wenn du so was (z.B. `__str__`) definierst,
> macht python im Hintergrund was komisches, und interpretiert es diese Methode als etwas ganz anderes.
> Man kann sich merken: **`str(object)` z.B. wird durch python als `object.__str__()` interpretiert.**

> Wenn du ein list `L = [1, 2, 3]` hast und `print(str(L))` schreibst, wird es im Hintergrund eigentlich
> als `print(L.__str__())` aufgeführt.
> Wenn eine Dundermethode auch ein / mehrere Argumente nimmt, dann ist es entweder
> - eine Vergleichung: z.B. `object.__lt__(other)` entspricht `objekt < other`, oder
> - eine Operation: z.B. `object.__add__(other)` entspricht `objekt + other`, oder
> - was anderes, z.B: `object.__getitem__(key)` entspricht `objekt[key]`,
>                     `object.__getattr__(attr)` entspricht `objekt.attr`,
>                     `object.__call__(arg)` entspricht `objekt(arg)` und so weiter, und so fort.
> Man kann so zu sagen alles selber definieren, was man mit ganz gewöhnten sachen,
> wie Funktionen, listen, Zahlen, etc. machen kann.
> Verrückt, ne?

## A2
Erweiter die Datenklasse BinaryNode um die Dundermethode `__str__`, konvertiere da alle Instanzen: `id`, `left` und `right` zu einem string, füge diese zueinander hinzu, und gib das Ergebnis zurück (mit einem return)! Was ist deine Beobachtung? Taucht hier Rekursion auf? Wenn ja, warum?
> Man hätte die Aufgabenstellung auch so formulieren können: `str(tree)` soll einen String zurückgeben, mit dem man die BinaryNode wieder einfach rekreieren kann.

> `tree = BinaryNode(1, BinaryNode(2, None, BinaryNode(3, None, None)), None)`

> `str(tree) == "BinaryNode(1, BinaryNode(2, None, BinaryNode(3, None, None)), None)"`

## A3
Erweiter die Datenklasse BinaryNode um die Methode `size`, welche uns zurückgeben soll, aus wievielen BinaryNodes unser Baum besteht. Man kann das sehr schön mit Rekursion schaffen. Du schaffst es! Was soll die Rekursionsargument von `size` sein? Wievielmal musst du `size` in sich selbst aufrufen?

`tree = BinaryNode(1, # erste
                   BinaryNode(2, # zweite
                              None, 
                              BinaryNode(3, # dritte
                                         None,
                                         None)),
                   None)`

`assert tree.size() == 3`

## A4
Erweiter die Datenklasse BinaryNode um die Methode `get_depth`, welche uns die Anzahl an BinaryNodes zurückgeben soll, die auf dem längsten Pfad von der Würzel aus zu finden sind. It's Rekursion, my dudes! Ich empfehle dir eine **optionale** Hilfsargument `depth` zu benutzen, wenn du ein "Rekursionsschicht tiefer gehst" (d.h. die Funktion in sich selbst aufrufst), kannst du `depth + 1` angeben und damit merken, wie tief wir sind.
- `depth` kann am Anfang als 1 (erste Schicht) initialisiert werden (`def ...(..., depth=1):`). 
Überlege einen sinnvollen Rückgabewert! Wie oft musst du `get_depth` in sich selbst aufrufen? An welche Stelle wäre es am sinnvollsten, sie aufzurufen?

`tree = BinaryNode(1, None, None)`

`tree.get_depth() == 1`

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.get_depth() == 3`

## A5
Erweiter die Datenklasse BinaryNode um die Methode `pre_order`, die uns eine Liste aller `id`s zurückgibt. Sodass die Liste zuerst die `id` von dem Wurzelknoten, dann alle `id`s des linken Teilbaumes `left`, und zum Schluss alle `id`s des rechten Teilbaumes `right` enthält. Die `id`s der Teilbäume soll wieder so sortiert sein wie oben beschrieben.
- Überlege einen sinnvollen Rückgabewert! Tip: listen kann man zueinander addieren: \[] + (\[1] + \[2]) + \[3] = \[1, 2, 3]

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.pre_order() == [1, 2, 3, 4]`
