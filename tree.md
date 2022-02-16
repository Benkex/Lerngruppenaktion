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
Erweiter die Datenklasse BinaryNode um die Methode `pre_order`, die uns eine Liste aller `id`s zurückgibt. Sodass die Liste zuerst die `id` von dem Wurzelknoten, dann alle `id`s des linken Teilbaumes `left`, und zum Schluss alle `id`s des rechten Teilbaumes `right` enthält. Die `id`s der Teilbäume soll wieder so sortiert sein wie oben beschrieben.

`tree = BinaryNode(1, BinaryNode(2, None, None), BinaryNode(3, None, BinaryNode(4, None, None)))`

`tree.pre_order() == [1, 2, 3, 4]`