
hoch2 = lambda n: n ** 2
potenz = lambda x, y: x ** y
add_operation = lambda x, y: x + y
mittelwert = lambda n: (sum(n) / len(n) if len(n) > 0 else 0)
teiler = lambda n: [i for i in range(1, abs(n) + 1) if n % i == 0]
gem_teiler = lambda x, y: [j for j in teiler(x) for i in teiler(y) if j == i]
tuplize = lambda x, y: (x, y)
kreuz = lambda x, y: [(m, n) for m in x for n in y]
nebenklasse = lambda v, U: {add_operation(v, n) for n in U}
sum_up = lambda n: (sum_up(n - 1) + n if n > 0 else 0)
fakultaet = lambda n: (n * fakultaet(n - 1) if n > 0 else 1)
# fibo = lambda n: [fibo(n - 2) + fibo(n - 1) if n > 1 else n]
fibo = lambda n: ([-fibo(x) for x in range(-1, -n-1, -1)]
		  if n >= 0 else fibo(n+1)+fibo(n+2)
		  if n < -2 else n+1)

def celsius_to_fahrenheit(deg_c):
    deg_f = (deg_c * 1.8 + 32)
    return deg_f


def fahrenheit_to_celsius(deg_f):
    deg_c = ((deg_f - 32) / 1.8)
    return deg_c


def celsius_to_kelvin(deg_c):
    deg_k = deg_c + 273.15
    return deg_k


def kelvin_to_celsius(deg_k):
    deg_c = deg_k - 273.15
    return deg_c


def fahrenheit_to_kelvin(deg_f):
    deg_c = fahrenheit_to_celsius(deg_f)
    deg_k = celsius_to_kelvin(deg_c)
    return deg_k


def kelvin_to_fahrenheit(deg_k):
    deg_c = kelvin_to_celsius(deg_k)
    deg_f = celsius_to_fahrenheit(deg_c)
    return deg_f

convert = {"c": {"f": celsius_to_fahrenheit, "k": celsius_to_kelvin},
            "f": {"c": fahrenheit_to_celsius, "k": fahrenheit_to_kelvin},
            "k": {"f": kelvin_to_fahrenheit, "c": kelvin_to_celsius}}


def repl_convert():
    vi: str = ""
    while True:
        vi: str = input("former unit: ")
        if vi == "quit":
            break
        vo: str = input("wanted unit: ")
        try:
            val = float(input("value to be converted: "))
            print(convert[vi][vo](val))
        except KeyError:
            print("please use valid units: c, f, k")
        except ValueError:
            print("please use valid value(float)")


if __name__ == "__main__":
    assert hoch2(8) == 64
    assert potenz(2, 3) == 8
    assert add_operation(2, 3) == 5
    assert mittelwert([2, 3]) == 2.5
    assert mittelwert([]) == 0
    assert teiler(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36], f"returns{teiler(36)}"
    assert teiler(0) == []
    assert teiler(-3) == [1 ,3]
    assert gem_teiler(12, 81) == [1, 3]
    assert gem_teiler(12, 23) == [1]
    assert gem_teiler(-5, 15) == [1, 5], f"returns{gem_teiler(-5,15)}"
    assert tuplize(3,5) == (3, 5)
    num = [1, 2, 3]
    let = ['x', 'y']
    assert kreuz(num, let) == [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y'), (3, 'x'), (3, 'y')]
    assert nebenklasse(3, [-8, 1, 5, -2, 0]) == {-5, 4, 8, 1, 3}
    assert sum_up(100) == 5050
    assert fakultaet(2) == 2
    assert fibo(2) == [[0, 1]], f"fib returns{fibo(2)}"
    repl_convert()
