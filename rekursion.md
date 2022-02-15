### REKURSION 
# Was ist Rekursion?
> Kennst du Fraktalbilder? Was man im exercise-05 machen musste,
> der Mandelbrot-Set war gerade ein Fraktal.
> Das bedeutet, du kannst die gleiche Muster sehen, wenn du reinzoomst.
> So ist es auch bei einer rekursiven Funktion: es ruft sich selbst auf,
> nur mit anderen Argumenten. Also quasi nochmal das ganze Bild
> in einem Teil des Bildes.
> Deshalb benutzt man gerne Rekursion, um einen Fraktal zu erstellen.
> Das werden wir schließlich auch machen. Aber erst arbeiten wir mit
> einfacheren Rekursionen.

## A1:
Erstelle eine Funktion `try_rekursion`, die als Argument eine ganze Zahl `n` nimmt.
- `try_rekursion` soll zuerst ihr Argument ausprinten, 
- dann sich selbst aufrufen mit `n + 1` oder `n - 1`, dem (Rekursionsargument).
Probier mal beide Optionen aus.
- Was ist deine Beobachtung?
erweitere `try_rekursion` so, dass das letzte was ausgeprintet wird, eine 0 ist! (Das ist die "Rekursionsstoppbedingung")
- Welche Rekursionsargument brauchst du, wenn das originelle `n` positiv ist?
- Und wenn es negativ ist? Du kannst eine if-Bedingung dafür schreiben!

## A2:
Erstelle eine Funktion `count_down`, die als Argument eine ganze Zahl `n` nimmt.
(`n` darf nicht negativ sein -> wenn es trotzdem negativ ist, erzeuge ein RuntimeError!).
- `count_down` soll zuerst ihr Argument ausprinten
- dann wenn `n > 1` gilt, sich selbst zurückgibt mit Argument `n - 1`
- ansonsten soll `count_down` einfach 1 zurückgeben

## A3:
Erstelle eine Funktion `count_to_n`, die als Argument eine ganze Zahl `n` nimmt.
- `count_to_n` soll zuerst ihr Argument ausprinten
- dann wenn `n > 1` gilt,  1 + sich selbst zurückgibt mit Argument `n - 1`
- ansonsten soll `count_to_n` einfach 1 zurückgeben
> Was gibt `count_to_n` am Ende zurück?

## A4:
Erstelle eine Funktion `double_up`, die als Argument eine ganze Zahl `n` nimmt.
- `double_up` soll zuerst ihr Argument ausprinten
- dann das zweifach ven sich selbst mit Argument `n - 1` zurückgibt, falls `n > 1` gilt.
- ansonsten soll 2 zurückgeben werden
> Was gibt `double_up` am Ende zurück?

## A5:
Erstelle eine Funktion `sum_up`, die als Argument eine ganze Zahl `n` nimmt.
und dann alle Zahlen von `n` bis `0` aufsummiert.(`n + (n - 1) + ... + 2 + 1 + 0`)
und diesen Wert dann zurückgibt.

## A6:
Erstelle eine rekursive Funktion `fakul`, die die Fakultät einer Zahl ausrechnet!
die Fakultät einer Zahl `n` berechnet sich als Produkt aller Zahlen von `1` bis `n`.
`n! = 1 * 2 * ...* (n - 1) * n`.
anschlieβend soll `fakul` den berechneten Wert zurückgeben.

## A7
Erstell eine rekursive Funktion `fib`, die eine ganze Zahl als Argument nimmt.
Und die n-te Fibonaccizahl berechnet.
Dabei gilt:
- `fib(0) = 0`
- `fib(1) = 1`
- `fib(n) = fib(n - 1) + fib(n - 2)
und diese zum Schluss zurückgibt.