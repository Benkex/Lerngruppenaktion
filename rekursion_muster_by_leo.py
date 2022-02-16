
#A1
def try_rekursion(n:int)->int:
    print(n)
    if n!=0:
        if n<0:
            try_rekursion(n+1)
        if n>0:
            try_rekursion(n-1)

#A2
def count_down(n:int)-> int:
    if n<0:
        raise RuntimeError("n must be greater than 0!")
    else:
        print(n)
        if n>1:
            return count_down(n-1)
        else:
            return 1
        
#A3
def count_to_n(n:int)->int:
    if n<0:
        raise RuntimeError("n must be greater than 0!")
    #print(n)
    if n>1:
        return 1+count_to_n(n-1)
    else:
        return 1
    
#A4
def double_up(n:int)->int:
    if n>1:
        return 2*double_up(n-1)
    else:
        return 2
    
#A5
def sum_up(n:int)-> int:
    if n<=0:
        return 0
    else:
        return n+sum_up(n-1)
    
#A6
def fakul(n:int)->int:
    if n<=0:
        return 1
    else:
        return n*fakul(n-1)
    
#A7
def fib(n:int)-> int:
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)