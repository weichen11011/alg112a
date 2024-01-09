## 有使用GPT輔助作業
import random

def neighbor(f, p, h):
    for i in range(len(p)):
        p[i] += random.uniform(-h, h)
    return p, f(p)

def hillclimbing(f, p, h=0.01):
    failcount = 0
    while failcount < 10:
        fnew = f(p)
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnew:  # 如果移動後高度比現在高
            fnew = f1  # 就移過去
            p = p1.copy()
            print('p=', p, 'f(p)=', fnew, 'count=', failcount)
            failcount = 0
        else:
            failcount += 1
    return p, fnew

# 定義新的n次多項式函數
def n_polynomial(p):
    # 定義 n 次多項式
    n = len(p)
    result = 0
    for i in range(n):
        result += p[i] ** (n - i)
    return result

# 使用 hillclimbing 函數解 n 次多項式
n = 4  # 修改為所需的 n 次多項式的次數
initial_guess = [2, 1, 3, 4]  # 初始化向量，元素數量為 n + 1

solution, value = hillclimbing(n_polynomial, initial_guess)
print("Solution:", solution)
print("Value:", value)
