def catalan(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    catalan_sum = 0
    for i in range(n):
        catalan_sum += catalan(i) * catalan(n - i - 1)
    return catalan_sum

n = int(input("N ni kiriting: "))
print(catalan(n))
