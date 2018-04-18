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

#�ɽ���k�ν���
import numpy as np
def max_profit_k(p,k):
    length=len(p)
    a=np.zeros([k + 1,length])
    b=np.zeros([k + 1,length])
    b[1:,0]=-p[0]#��ʼֵ
    for i in range(1,k+1):
        for n in range(1,length):
            a[i,n]=np.max([a[i,n-1],b[i,n-1]+p[n]])#��n��(�������0���൱����ʵ��ĵ�1��)���������i�ν��ף�������档
            b[i,n]=np.max([b[i,n-1],a[i-1][n-1]-p[n]])#��n�죬�������i-1�Ӱ�ν��ף�������棬b[i,n]�����һ�ν��ױ�������
    return a[k,length-1]


p=[2,3,4,1,2,5,1,3]
max_profit_k(p,2)

#����
import numpy as np
def max_profit_2(p):
    todo

p=[2,3,4,1,2,5]
max_profit_2(p)


#4.������
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