from micrograd.engine import Value

a = Value(2)
b = Value(1)
c = Value(3)

while (a > 0.01):
    step = 0.01
    f = a**2 + b**2 + c**2
    print('f(p) = {}, p = [{}, {}, {}]'.format(f.data, a.data, b.data, c.data))
    f.backward()
    
    ## 重新尋找新的梯度
    a -= a.grad * step  
    b -= b.grad * step
    c -= c.grad * step
    
print('f(p) = {}, p = [{}, {}, {}]'.format(f.data, a.data, b.data, c.data))
