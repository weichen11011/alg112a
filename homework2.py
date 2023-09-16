def power2n(n):
    return 2**n
def power2n1(n):
    if n == 0 :
        return 1
    if n == 1 :
        return 2
    return power2n1(n-1) + power2n1(n-1)
def power2n2(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    else:
        return 2*power2n2(n-1)    

fib = [None]*10000
fib[0] = 1
fib[1] = 1
def power2n3(n):
    if n <0: return False
    if not fib[n] is None:
        return fib[n]
    fib[n] = power2n3(n-1) + power2n3(n-1)
    return fib[n]

print(power2n1(10))
print(power2n2(11))
print(power2n3(11))
