from asyncio.windows_events import INFINITE
from typing import Iterator
from random import randint

from rekursion_muster import fakul


mul_3 = [i * 3 for i in range(1, 8)]
print(f"{mul_3=}")

pot_3 = [3 ** i for i in range(6)]
print(f"{pot_3=}")

abc = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(f"{abc=}")

ABC = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(f"{ABC=}")

mul_3_doppelt_ungerade = [i * 2 for i in mul_3 if i % 2 == 1]
print(f"{mul_3_doppelt_ungerade=}")

listen = [[] for _ in range(5)]
print(f"{listen=}")

armband = [[8] for _ in range(5)]
print(f"{armband=}")

tictactoe = [['.' for _ in range(3)] for _ in range(3)]
print(f"{tictactoe=}")

telephone = [[i + j * 3 for i in range(1, 4)] for j in range(3)]
print(f"{telephone=}")

telephone_1 = [i for inner in telephone for i in inner]
print(f"{telephone_1=}")

telephone_2 = [i for inner in telephone[::-1] for i in inner]
print(f"{telephone_2=}")

telephone_3 = [i for inner in telephone for i in inner[::-1]]
print(f"{telephone_3=}")


def my_generator_1(n: int) -> Iterator[int]:
    for i in range(1, 21):
        yield n * i


print(f"{list(my_generator_1(3))=}")


def my_generator_2(n: int) -> Iterator[int]:
    for i in range(1, 21):
        yield i ** n


print(f"{list(my_generator_2(3))=}")


def my_generator_3(n: int) -> Iterator[int]:
    for i in range(1, n + 1):
        yield fakul(i)


print(f"{list(my_generator_3(6))=}")
n = 3
genc_1 = (i * n for i in range(1, 21))
print(f"{next(genc_1)=}")

genc_2 = (i ** n for i in range(1, 21))
print(f"{next(genc_2)=}")

gen_3 = (fakul(i) for i in range(1, n + 1))

genc_4 = (zeile for zeile in telephone)
print(f"{next(genc_2)=}")

farbe = {"Spiegel": "grün", "Wand": "weiß", "Banane": "gelb", "Käse": "gelb"}

print(f"{list(farbe)=}")
print(f"{list(farbe.values())=}")
print(f"{list(farbe.items())=}")

farbe_anzahl: dict[str, int] = {}
for _, v in farbe.items():
    farbe_anzahl[v] = farbe_anzahl.get(v, 0) + 1
print(farbe_anzahl)

str_int = {chr(randint(97, 97+26))*4: randint(0, 100) for _ in range(8)} 
str_float = {key: float(val) for key, val in str_int.items()}
str_double = {
    key: val * 2
    for key, val in zip(str_int.keys(), str_int.values())
}
print(str_int)
print(str_float)
print(str_double)
