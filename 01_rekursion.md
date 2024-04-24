### REKURSION 
# Was ist Rekursion?
> Kennst du Fraktalbilder? Was man im exercise-05 machen musste,
> der Mandelbrot-Set war gerade ein Fraktal.
> Das bedeutet, du kannst die gleiche Muster sehen, wenn du reinzoomst.
> So ist es auch bei einer rekursiven Funktion: es ruft sich selbst auf,
> nur mit anderen Argumenten. Also quasi nochmal das ganze Bild
> in einem Teil des Bildes.
> (Deshalb benutzt man gerne Rekursion, um Fraktalbilder zu erstellen.)

## A1 (Beispielaufgabe:)
### A1.1 
Erstelle eine Funktion `try_rekursion`, die als Argument eine ganze Zahl `n` nimmt.
  ```py
  def try_recursion(n: int):
  ```
- `try_rekursion` soll zuerst ihr Argument ausprinten, 
  ```py
  def try_recursion(n: int):
      print(n)
  ```
- dann sich selbst aufrufen mit `n + 1`.
  ```py
  def try_recursion(n: int):
      print(n)
      try_recursion(n + 1)
  ```
!!! Neuer Begriff:  `try_recursion(n + 1)` nennen wir hier _"rekursiver Aufruf"_ !!!

- Was ist deine Beobachtung?  
  (Du kannst es mit der Tastenkombination `Ctrl + C` stoppen)  
  Probiere jetzt mit `n - 1`.
  ```py
  def try_recursion(n: int):
      print(n)
      try_recursion(n - 1)
  ```
- Was ist deine Beobachtung?  
!!! Neuer Begriff:  `n + 1` und `n - 1` nennen wir hier _"Rekursionsargument"_, weil es der Argument des rekursiven Aufrufs ist !!!

### A1.2 
Erweitere `try_rekursion` so, dass sie bis 0 zählt!
- Was, wenn das originelle `n` positiv ist? Welche Rekursionsargument brauchst du?
- Und wenn `n` negativ ist? Du kannst if-Bedingungen dafür schreiben!
```py
def try_recursion(n: int):
    print(n)
    if n < 0:
        try_recursion(n + 1)
    elif n > 0:
        try_recursion(n - 1)
```
!!! Neuer Begriff: `n < 0` nennen wir hier _"Rekursions-stop-bedingung"_ (Rekursionsstopbedingung) !!!



## A2 (Beispielaufgabe:)
Erstelle eine Funktion `count_down`, die als Argument eine *positive* ganze Zahl `n` nimmt,  
( `n` darf nicht negativ sein -> das kannst Du mit `assert` kontrollieren:
```py
def count_down(n: int):
    assert n >= 0, "n muss >= 0 sein!"
```
Versuche mal z.B. `count_down(-3)` aufzurufen!  
) und...
- erst `n` ausgibt (printet),
  ```py
  def count_down(n: int):
      assert n >= 0, "n muss >= 0 sein!"
      print(n)
  ```
- dann einen rekursiven Aufruf macht mit Rekursionsargument `n - 1`, das Ergebnis in einer Variable speichert, und zurückgibt
  ```py
  def count_down(n: int):
      assert n >= 0, "n muss >= 0 sein!"
      print(n)
      result = count_down(n - 1)
      return result
  ```
  !!! Neuer Begriff: `result` (den Rückkehrwert vom rekursiven Aufruf) nennen wir hier _"Rekursionsergebnis"_ !!!  

> Was gibt `count_down` zurück, wenn ich sie mit `6` aufrufe? (Probiere `result = count_down(6)` und `print(result)` ! )  
> Und mit `12`? (Probiere `result = count_down(12)` und `print(result)` ! )  
> Denke über das Ergebnis nach! Warum ist das rausgekommen und wie?

---

Ok, Du bist dran! :-)

---

## A3:
Erstelle eine Funktion `count_to_n`, die als Argument eine *positive* ganze Zahl `n` nimmt. ( `n` darf nicht negativ sein! )
- `count_to_n` soll zuerst ihr Argument ausprinten
- dann wenn `n > 1` gilt,  1 + sich selbst zurückgibt mit Argument `n - 1`
- ansonsten soll `count_to_n` einfach 1 zurückgeben
> Was gibt `count_to_n` am Ende zurück?

## A4:
Erstelle eine Funktion `two_to_the`, die als Argument eine *positive* ganze Zahl `n` nimmt. ( `n` darf nicht negativ sein! )  
Diese Funktion soll 2^n (2 hoch n) zurückgeben. Wenn `n > 0`, die Funktion soll einen rekursiven Aufruf machen mit Rekursionsargument `n - 1`,
dann das Rekursionsergebnis davon mit `2` multiplizieren und das Endergebnis zurückgeben.
Sonst soll die Funktion 1 zurückgeben.

## A5:
Erstelle eine Funktion `sum_up`, die als Argument eine *positive* ganze Zahl `n` nimmt, ( `n` darf nicht negativ sein! )  
dann alle Zahlen von `n` bis `0` aufsummiert (`n + (n - 1) + ... + 2 + 1 + 0`) und diesen Wert dann zurückgibt.

## A6:
Erstelle eine rekursive Funktion `fakul`,  die als Argument eine *positive* ganze Zahl `n` nimmt ( `n` darf nicht negativ sein! )
und die Fakultät von n ausrechnet! Die Fakultät einer Zahl `n` berechnet sich 
als Produkt aller Zahlen von `1` bis `n`.

`n! = 1 * 2 * ...* (n - 1) * n`.

anschlieβend soll `fakul` den berechneten Wert zurückgeben.

## A7
Erstell eine rekursive Funktion `fib`, die als Argument eine *positive* ganze Zahl `n` nimmt,
Und die n-te Fibonaccizahl berechnet.
Dabei gilt:
- `fib(0) = 0`
- `fib(1) = 1`
- `fib(n) = fib(n - 1) + fib(n - 2)`

und diese zum Schluss zurückgibt.
