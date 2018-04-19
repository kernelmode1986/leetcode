#input:cnblogs,belong
#最长公共子序列为blog（cnblogs,belong）
#最长公共子串为lo（cnblogs, belong）
#最长公共子序列（Longest Common Subsequence,LCS），顾名思义，是指在所有的子序列中最长的那一个。
#子串是要求更严格的一种子序列，要求在母串中连续地出现。

import numpy as np
def lcs_1(a,b):
    len_a=len(a)
    len_b=len(b)
    if len_a==0 or len_b==0:
        return 0
    dp=np.zeros([len_a,len_b])
    for i in range(len_a):
        for j in range(len_b):
            if i==0 or j==0:
                if a[i]==b[j]:
                    dp[i,j]=1
                else:
                    dp[i,j]=0
            else:
                if a[i]==b[j]:
                    dp[i,j]=dp[i-1,j-1]+1
                else:
                    dp[i,j]=np.max([dp[i-1,j],dp[i,j-1]])  
    return dp[len_a-1,len_b-1]
a='cnblogs'
b='belong'
lcs_1(a,b)


import numpy as np
def lcs_2(a,b):
    len_a=len(a)
    len_b=len(b)
    if len_a==0 or len_b==0:
        return 0
    dp=np.zeros([len_a,len_b])
    res=0
    for i in range(len_a):
        for j in range(len_b):
            if i==0 or j==0:
                if a[i]==b[j]:
                    dp[i,j]=1
                else:
                    dp[i,j]=0
            else:
                if a[i]==b[j]:
                    dp[i,j]=dp[i-1,j-1]+1
                else:
                    dp[i,j]=0
            res=np.max([res,dp[i,j]])
    return res
a='cnblogs'
b='belong'
lcs_2(a,b)