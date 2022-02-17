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
Erweiter die Datenklasse BinaryNode um die Dundermethode `__str__`, konvertiere da alle Instanzen: `id`, `left` und `right` zu string Typ, füge diese zueinander hinzu, und gib das Ergebnis zurück (mit einem return)! Was ist deine Beobachtung? Taucht hier Rekursion auf? Wenn ja, warum?
> Man hätte die Aufgabenstellung auch so formulieren können: `str(tree)` soll einen String zurückgeben, mit dem man die BinaryNode wieder einfach rekreieren kann.

`tree = BinaryNode(1, BinaryNode(2, None, BinaryNode(3, None, None)), None)`

`str(tree) == "BinaryNode(1, BinaryNode(2, None, BinaryNode(3, None, None)), None)"`

## A3
Erweiter die Datenklasse BinaryNode um die _rekursive_ Methode `size`, welche uns zurückgeben soll, aus wievielen BinaryNodes unser Baum besteht. Man kann das sehr schön mit Rekursion schaffen. Du schaffst es! Was soll die _Rekursionsargument_ von `size` sein? Wievielmal musst du `size` in sich selbst aufrufen?

`tree = BinaryNode(1, # erste
                   BinaryNode(2, # zweite
                              None, 
                              BinaryNode(3, # dritte
                                         None,
                                         None)),
                   None)`

`assert tree.size() == 3`

## A4
Erweiter die Datenklasse BinaryNode um die _rekursive_ Methode `depth`, welche uns die Anzahl an BinaryNodes zurückgeben soll, die auf dem längsten Pfad von der Würzel aus zu finden sind.

Überlege einen sinnvollen Rückgabewert! Wie oft musst du `depth` in sich selbst aufrufen? An welche Stelle wäre es am sinnvollsten, sie aufzurufen?

`tree = BinaryNode(1, None, None)`

`tree.depth() == 1`

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.depth() == 3`

## A5
Erweiter die Datenklasse BinaryNode um die _rekursive_ Methode `pre_order`, die uns eine Liste aller `id`s zurückgibt. Sodass die Liste zuerst die `id` von dem Wurzelknoten, dann alle `id`s des linken Teilbaumes `left`, und zum Schluss alle `id`s des rechten Teilbaumes `right` enthält. Die `id`s der Teilbäume soll wieder so sortiert sein wie oben beschrieben.
- Überlege einen sinnvollen Rückgabewert! Tip: listen kann man zueinander addieren: \[] + (\[1] + \[2]) + \[3] = \[1, 2, 3]

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.pre_order() == [1, 2, 3, 4]`

## A5.2
Erweiter die Datenklasse BinaryNode um die _rekursive_ Methode `post_order`, die uns eine Liste aller `id`s zurückgibt. Sodass die Liste 
- zuerst alle `id`s des linken Teilbaumes `left`,
- dann alle `id`s des rechten Teilbaumes `right`,
- und zum Schluss die `id` von dem Wurzelknoten enthält.
Die `id`s der Teilbäume soll wieder so sortiert sein wie oben beschrieben.

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.post_order() == [2, 4, 3, 1]`

## A6
Erweiter die Datenklass BinaryNode um die _rekursive_ Methode `flip`, die uns den Baum umdreht. Umdrehen heißt, dass für jeden Knoten der rechte mit dem linken Teilbaum vertauscht wird.
Tip: In Python vertauscht man Sachen gerne so: x, y = y, x. Reicht das für diese Aufgabe? Wie wird die Methode rekursiv?

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.flip()`

`str(tree) == str(BinaryNode(1, BinaryNode(3, BinaryNode(4, None, None), None), BinaryNode(2, None, None)))`

# Suchbäume
Als nächstes wollen wir uns einen speziellen Binärbaum anschauen, den Suchbaum.
Ein Suchbaum unterscheidet sich von einem Binärbaum nur in dem Detail, dass in Suchbäumen
- die `id`s des linken Teilbaumes (was jetzt `lower` heißen soll) immer kleiner sind als die `id` des Elternknotens, und
- die `id`s des rechten Teilbaumes (was jetzt `higher` heißen soll) sind immer größer.
Diese sind die _Suchbaumbedingungen_.

## A7
Schreibe die _rekursive_ Funktion `insert(tree: Optional[BinaryNode], new_id: int)`, die die `new_id` in den Baum so einfügt, dass die _Suchbaumbedingungen_ erfüllt bleiben (d.h. du kannst `new_id` immer mit dem entsprechenden `id` vergleichen, dann "eine Rekursionsschicht niedriger gehen", und dabei die Rekursionsargument entsprechend wählen), und den resultierenden Suchbaum zurück gibt. 
- Falls `tree` None ist soll ein Suchbaum erstellt werden.
- Wenn die `new_id` schon existiert soll der Baum ungeändert wieder ausgegeben werden.
Tip: was

`tree = BinaryNode(3, BinaryNode(2, None, None), BinaryNode(4, None, BinaryNode(5, None, None)))`

`insert(tree, 1)` => `tree` sieht so aus: `BinaryNode(3, BinaryNode(2, None, None), BinaryNode(4, None, BinaryNode(5, None, None)))`

## A8
Schreibe die Funktion `create_tree`, welche aus einer Liste an `id`s einen Suchbaum erstellt.

`ids = [5, 1, 4, 3, 5, 7, 9]`
`create_tree(ids) == BinaryNode(5, BinaryNode(1, None, 
                                                 BinaryNode(4, BinaryNode(3, None, None), 
                                                               None)),
                                   BinaryNode(7, None, 
                                                 BinaryNode(9, None, None)))`

## A9
Schreibe die Funktion `find`, welche einen `tree` und eine `id` als Argumente nimmt. `find` soll die BinaryNode Objekt im Suchbaum finden, bei dem die `id` übereinstimmt und diese Objekt dann zurückgeben. Nutze dafür die Struktur des Suchbaumes. Wenn die `id` im Suchbaum nicht gefunden wurde soll None zurück gegeben werden.

## A10
Schreibe die Funktion `select`, die aus einem Suchbaum `tree` alle `id`s ausgibt für die gilt, `lower <= id <= higher`. Die `id` sollen aufsteigend soltiert sein, nutze dafür allerdings **nicht** sort, oder sorted.

# Allgemeine Bäume
Binärbaume haben ja bis zu 2 Kindern, bei allgemeinen Bäumen ist dies nicht der Fall, hier kann die Anzahl der Kinder beliebig sein, und auch viel größer als 2 wenn wir also jedes Kind in einem extra Attribut speichern, haben wir eine Menge schreibaufwand. Wir werde aus dem Grund unsere Kinder in einer Liste speichern.

## A11
Ergänze die Datenklasse Node um die folgenden Attribute:
- `id` welches eine ganze Zahl ist
- `children` eine Liste die alle Kinder des Knoten beinhaltet

## A12
Implementiere wie auch in der BinaryNode die Dundermethode `__str__` um die Nodes wieder leserlich ausgeben zu können.

## A13
Implementiere die Methode `weight`, die uns alle `id`s zusammen addiert.

## A14
Implementiere die Funktion `on_layer`, die einen Baum `tree` nimmt und uns alle `id`s zurück gibt, die auf der Ebene sind mit gegebener Tiefe `depth`.
