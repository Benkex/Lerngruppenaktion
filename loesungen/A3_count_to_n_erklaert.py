
#              5 <---
def count_to_n(n: int) -> int:
    if n>1:
        return 1 + count_to_n(n-1) # = 1 + (1 + (1 + (1 + 1))) # n-1 = 4
        #          if n>1: # n = 4
        #              return 1 + count_to_n(n-1) = 1 + (1 + (1 + 1)) # n-1 = 3
        #                         if n>1: # n = 3
        #                             return 1 + count_to_n(n-1) = 1 + (1 + 1) # n-1 = 2
        #                                        if n>1: # n = 2
        #                                            return 1 + count_to_n(n-1) = 1 + 1 # n-1 = 1
        #                                                       if n>1: # n = 1
        #                                                           # NICHT DER FALL
        #                                                       else:
        #                                                           return 1 # DER FALL!
    else:
        return 1
