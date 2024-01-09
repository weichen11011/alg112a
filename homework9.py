def conflict(state, nextX):    
    nextY = len(state)
    
    ## 同行
    if any(abs(state[i] - nextX) == 0 for i in range(len(state))):
        return True
    
    ## 同一對角線
    if any(abs(state[i]-nextX) - abs(i - nextY) == 0 for i in range(len(state))):
        return True
    
    ## 未發生碰種 回傳
    return False

def queens(n,state = ()):
    ## 排完了 清空找尋下一個數組
    if len(state) == n:
        return [()]
    ans = []
    for x in range(n):
        ## 若都沒有發生碰撞，將點記錄起來後並尋找下一列
        if not conflict(state, x):
            ## 記錄新皇后的位置
            for result in queens(n,state + (x,)):
                ans += [(x,) + result]
    return ans

def pic(n,state):
    for pos in state:
        print("===================")
        for i in range(n):
            for j in range(n):
                if pos[i] == j:
                    print("Q",end='')
                else:
                    print(".",end='')
            print(end='\n')        
            
        
## print(queens(8))
pic(8,queens(8))
