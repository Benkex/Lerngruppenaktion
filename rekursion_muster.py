def try_rekursion(n: int) -> int:
    print(n)
    if n != 0:
        if n < 0:
            try_rekursion(n + 1)
        if n > 0:
            try_rekursion(n - 1)


def count_down(n: int) -> int:
    if n < 0:
        raise RuntimeError("n must be greater than 0!")
    
    print(n)
    if n > 1:
        return count_down(n - 1)
    
    return 1


def count_to_n(n: int) -> int:
    print(n)
    if n > 1:
        return 1 + count_to_n(n - 1)
    
    return 1


def double_up(n: int) -> int:
    print(n)
    if n > 1:
        return 2 * double_up(n - 1)
    
    return 2


def sum_up(n: int) -> int:
    return n + sum_up(n - 1) if n > 0 else 0


def fakul(n: int) -> int:
    return n * fakul(n - 1) if n > 0 else 1


def fib(n: int) -> int:
    return fib(n - 1) + fib(n - 2) if n > 1 else n


if __name__ == "__main__":
    print(f"{try_rekursion(5)=}")
    print(f"{count_down(5)=}")
    print(f"{count_to_n(5)=}")
    print(f"{double_up(5)=}")
    print(f"{sum_up(5)=}")
    print(f"{fakul(5)=}")
    print(f"{fib(5)=}")