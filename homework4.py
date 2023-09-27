import math
from numpy import arange
def solution(n):
    ans = n**2 - 3*n +1
    return ans
for i in arange(-100,100,0.001):
    if abs(solution(i)) < 0.001:
        print("x=", i, " f(x)=", solution(i)) 
