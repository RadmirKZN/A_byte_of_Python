def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    print(total)

powersum(2, 3, 4, 9)
