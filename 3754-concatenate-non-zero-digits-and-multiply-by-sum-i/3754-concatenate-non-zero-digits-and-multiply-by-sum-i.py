class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        l=str(n)
        s=0
        k='0'
        for i in l:
            if i!='0':
                k+=i
                s+=int(i)
        k=int(k)
        return k*s
        