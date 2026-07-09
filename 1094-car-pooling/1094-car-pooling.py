class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        a=[0]*1001
        s=0
        for i,j,k in trips:
            a[j]+=i
            a[k]-=i
        for i in range(1001):
            s+=a[i]
            if s>capacity:
                return False
        return True
        