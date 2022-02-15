# ##################### REKURSION ########################
# Was ist Rekursion?
#   Kennst du Fraktalbilder? Was man im exercise-05 machen musste,
# der Mandelbrot-Set war gerade ein Fraktal.
# Das bedeutet, du kannst die gleiche Muster sehen, wenn du reinzoomst.
#   So ist es auch bei einer rekursiven Funktion: es ruft sich selbst auf,
# nur mit anderen Argumenten. Also quasi nochmal das ganze Bild
# in einem Teil des Bildes.
#   Deshalb benutzt man gerne Rekursion, um einen Fraktal zu erstellen.
# Das werden wir schließlich auch machen. Aber erst arbeiten wir mit
# einfacheren Rekursionen.

# A1:
# Erstelle eine Funktion mit einem Argument "n", die erst mal ihre Argument
# ausprintet, dann sich selbst aufruft, nur mit Argument "n-1"
# oder "n+1" (Rekursionsargument).
#   Probier mal beide aus.
#   Was ist deine Beobachtung?
# Schreibe eine if-Bedingung dafür, so dass das letzte was ausgeprintet wird,
# ein 0 ist! (Das ist die "Rekursionsstoppbedingung")
#   Welche Rekursionsargument brauchst du, wenn das originelle "n" positiv ist?
#   Und wenn es negativ ist? Du kannst eine if-Bedingung dafür schreiben!

# A2:
# Erstelle eine Funktion mit einem Argument "n" (darf nicht negativ sein ->
# wenn es trotzdem negativ ist, erzeuge ein RuntimeError!), die erst mal
# ihre Argument ausprintet, dann als Rückkehrwert sich selbst
# mit Argument "n-1" aufruft, falls n > 1.
# Andernfalls soll sie 1 zurückgeben.

# A3:
# Erstelle eine Funktion mit einem Argument "n", die erst mal ihre Argument
# ausprintet, dann als Rückkehrwert 1 + sich selbst (mit Argument n-1)
# zurückgibt, falls n > 1.
# Andernfalls soll sie 1 zurückgeben.
# Was gibt es am Ende zurück?

# A4:
# Erstelle eine Funktion mit einem Argument "n", die erst mal ihre Argument
# ausprintet, dann als Rückkehrwert die zweifache von sich selbst (mit Argument n-1)
# zurückgibt, falls n > 1.
# Andernfalls soll sie 2 zurückgeben.
# Was gibt es am Ende zurück?

# A5:
# Erstelle eine Funktion mit einem Argument "n", die die Zahlen 0 bis n
# summiert!

# A6:
# Erstelle eine rekursive Funktion, die die Fakultät einer Zahl ausrechnet!
