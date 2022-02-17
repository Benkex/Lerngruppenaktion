### Bäume
> In den kommenden Aufgaben, wollen wir uns eine Übersicht über Bäume erschaffen.
> Dazu erstellen wir uns erst einen einfachen Binärbaum, und gehen später über zu allgemeinen Bäumen.
> Unterdessen schauen wir uns an wie man auf Bäumen arbeiten kann.
> Zur Unterstützung kann das in tree.py bereitgestellte Template verwendet werden.
> Dabei soll stetig auf richtiges Typing geachtet werden.

## A1
Ergänze die Datenklasse BinaryNode um die Attribute `id` welches eine ganze Zahl nimmt, `left` welches entweder wieder eine `BinaryNode` nimmt oder `None`, und `right` welches wie left wieder `BinaryNode` oder `None` nimmt.

## A2
Erweiter die Datenklasse BinaryNode um die Dundermethode `__str__()`, sodass `str(tree)` einen String zurückgibt, mit dem man die BinaryNode wieder einfach rekreieren kann.

`tree = BinaryNode(1, BinaryNode(2, None, BinaryNode(3, None, None)), None)`

`str(tree) == "BinaryNode(1, BinaryNode(2, None, BinaryNode(3, None, None)), None)"`

## A3
Erweiter die Datenklasse BinaryNode um die Methode `size`, welche uns zurückgibt aus wievielen BinaryNodes unser Baum besteht.

`tree = BinaryNode(1, BinaryNode(2, None, BinaryNode(3, None, None)), None)`

`tree.size() == 3`

## A4
Erweiter die Datenklasse BinaryNode um die Methode `depth`, welche uns die Anzahl an BinaryNodes zurückgibt, die auf dem längsten Pfad von der Würzel aus zu finden sind.

`tree = BinaryNode(1, None, None)`

`tree.depth() == 1`

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.depth() == 3`

## A5
Erweiter die Datenklasse BinaryNode um die Methode `post_order`, die uns eine Liste aller `id`s zurückgibt. Sodass die Liste zuerst alle `id`s des linken Teilbaumes `left`, dann alle `id`s des rechten Teilbaumes `right`, und zum Schluss die `id` von dem Wurzelknoten enthält. Die `id`s der Teilbäume soll wieder so sortiert sein wie oben beschrieben.

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.post_order() == [2, 4, 3, 1]`

## A6
Erweiter die Datenklass BinaryNode um die Methode `flip`, die uns den Baum umdreht. Umdrehen heißt, dass für jeden Knoten der rechte mit dem linken Teilbaum vertauscht wird.

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.flip()`

`str(tree) == str(BinaryNode(1, BinaryNode(3, BinaryNode(4, None, None), None), BinaryNode(2, None, None)))`

### Suchbäume
Als nächstes wollen wir uns einen speziellen Binärbaum anschauen, den Suchbaum.
Ein Suchbaum unterscheidet sich von einem Binärbaum nur in dem Detail, dass in Suchbäumen, die `id`s des linken Teilbaumes immer kleiner sind als die `id` des Elternknotens, und die `id`s des rechten Teilbaumes sind immer größer.

## A7
Schreibe die Funktion `insert(tree: Optional[BinaryNode], id: int)`, die die `id` in den Baum so einfügt, dass die Suchbaumbedingungen erfüllt bleiben. Und den resultierenden Suchbaum zurückgibt, falls `tree` None ist soll ein Suchbaum erstellt werden.

## A8
Schreibe die Funktion `create_tree`, welche aus einer Liste an `id`s einen Suchbaum erstellt.

## A9
Schreibe die Funktion `find`, welche einen `tree` und eine `id` als Argumente nimmt. `find` soll die BinaryNode im Suchbaum finden, bei dem die `id` übereinstimmt und diese dann zurück gibt. Nutze dafür die Struktur des Suchbaumes. Wenn die `id` im Suchbaum nicht gefunden wurde soll None zurück gegeben werden.

## A10
Schreibe die Funktion `select`, die aus einem Suchbaum `tree` alle `id`s ausgibt für die gilt, lower <= id <= upper. die `id` sollen aufsteigend soltiert sein, nutze dafür allerdings nicht sort, oder sorted.

