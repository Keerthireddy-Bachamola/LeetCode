from collections import *
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        print(indegree)
        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x]+=1
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        c=0
        while q:
            c+=1
            x=q.popleft()
            for nei in graph[x]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return c==numCourses
            
        
        
        