def p16():
    num = 2**1000
    total = 0
    for x in str(num):
        total += int(x)
    print(total)
