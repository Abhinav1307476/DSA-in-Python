def printNumber(lb, ub):
    printNumber(lb + 1, ub)
    if lb > ub:
        return
    print(lb)

printNumber(1, 3)