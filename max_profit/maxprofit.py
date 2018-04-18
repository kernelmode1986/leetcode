import numpy as np
def max_profit_1(p):
    length=len(p)
    a=np.zeros(length)
    min_p=p[0]
    for i in range(1,length):
        min_p=np.min([min_p,p[i-1]])
        a[i]=np.max([a[i-1],p[i]-min_p])
    return a[i]

p=[2,3,4,1,2,5]
max_profit_1(p)

#可进行k次交易
import numpy as np
def max_profit_k(p,k):
    length=len(p)
    a=np.zeros([k + 1,length])
    b=np.zeros([k + 1,length])
    b[1:,0]=-p[0]#初始值
    for i in range(1,k+1):
        for n in range(1,length):
            a[i,n]=np.max([a[i,n-1],b[i,n-1]+p[n]])#第n天(视这里第0天相当于现实里的第1天)，完成至少i次交易，最大收益。
            b[i,n]=np.max([b[i,n-1],a[i-1][n-1]-p[n]])#第n天，完成至少i-1加半次交易，最大收益，b[i,n]的最后一次交易必须是买。
    return a[k,length-1]


p=[2,3,4,1,2,5,1,3]
max_profit_k(p,2)

#两次
import numpy as np
def max_profit_2(p):
    todo

p=[2,3,4,1,2,5]
max_profit_2(p)


#4.任意多次
import numpy as np
def max_profit_n(p):
    length=len(p)
    profit=0
    for i in range(1,length):
        if p[i]>p[i-1]:
            profit=profit+p[i]-p[i-1]
    return profit

p=[2,3,4,1,2,1,5]
max_profit_n(p)