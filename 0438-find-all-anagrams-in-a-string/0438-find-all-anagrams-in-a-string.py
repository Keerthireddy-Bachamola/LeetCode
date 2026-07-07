class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        r=[]
        if len(p)>len(s):
            return []
        d=Counter(p)
        i=0
        n=len(s)
        m=len(p)
        dd={}
        for j in range(n):
            dd[s[j]]=dd.get(s[j],0)+1
            if j-i+1==m:
                if d==dd:
                    r.append(i)
                dd[s[i]]-=1
                if dd[s[i]]==0:
                    del dd[s[i]]
                i+=1
        return r




        
        