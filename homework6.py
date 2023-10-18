import random

def neighber(f,p,h):
    for i in range(len(p)):
        p[i]+= random.uniform(-h, h)
    return p,f(p)
        
def hillclimbing(f,p,h=0.01):
    failcount=0
    while(failcount<10):
        fnew = f(p)
        p1,f1 = neighber(f,p,h)
        if f1 >= fnew:               # 如果移動後高度比現在高
            fnew = f1                #   就移過去
            p = p1.copy()
            print('p=', p, 'f(p)=', fnew,'count=',failcount)
            failcount = 0
        else:
            failcount+=1
    return (p,fnew)         
            
def f(p):
    return -1*(p[0]**2+p[1]**2+p[2]**2)   

hillclimbing(f,[2,1,3])  
