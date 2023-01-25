from typing import Iterator

def knapsack(goal:int, items:list[tuple[str,int]]) -> Iterator[list[str]]:
    if goal == 0:
        yield []  # solution found
    elif not items:
        return  # out of items, no solution
    else:
        item0, weight = items[0]  # a, 6
        remaining_items = items[1:]
        for k in knapsack(goal, remaining_items):  # solutions without item0
            yield k
        if weight <= goal:
            for solution in knapsack(goal - weight, remaining_items):
                yield [item0] + solution

namen = [chr(97+i) for i in range(10)]
#        a  b   c   d   e   f  g  h  i  j
werte = [6, 21, 12, 13, 34, 5, 7, 4, 9, 10]
# 34 + 5 + 7 + 10 = 56
# print(list(zip(namen, werte)))
for loesung in knapsack(56, list(zip(namen, werte))):
    print(loesung)
