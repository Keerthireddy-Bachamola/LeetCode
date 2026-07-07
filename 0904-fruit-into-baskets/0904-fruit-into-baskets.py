class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        d={}
        i=0
        m=0
        for j in range(n):
            d[fruits[j]]=d.get(fruits[j],0)+1
            while len(d)>2:
                d[fruits[i]]-=1
                if d[fruits[i]]==0:
                    del d[fruits[i]]
                i+=1
            m=max(m,j-i+1)
        return m

        