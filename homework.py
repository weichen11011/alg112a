from datetime import datetime
def fibonacci (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    count = 0
    for i in range(2,n+1):
        count = a + b
        a = b
        b = count
    return count
n=60
startTime = datetime.now()
print(f'fibonacci({n})={fibonacci(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
