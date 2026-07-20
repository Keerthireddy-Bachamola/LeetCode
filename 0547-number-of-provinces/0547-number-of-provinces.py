class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        def dfs(node):
            visited.add(node)
            for neighbour in range(len(isConnected[node])):
                if isConnected[node][neighbour]==1 and neighbour not in visited:
                    dfs(neighbour)
        c=0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                c+=1
        return c
        