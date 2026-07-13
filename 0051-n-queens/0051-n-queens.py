class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows,col,posd,negd=set(),set(),set(),set()
        board=[['.']*n for i in range(n)]
        res=[]
        def fun(i):
            if i==n:
                res.append([''.join(p) for p in board])
                return
            for j in range(n):
                if i in rows or j in col or i+j in posd or i-j in negd or board[i][j]=='Q':
                    continue
                board[i][j]='Q'
                rows.add(i)
                col.add(j)
                posd.add(i+j)
                negd.add(i-j)
                fun(i+1)
                board[i][j]='.'
                rows.discard(i)
                col.discard(j)
                posd.discard(i+j)
                negd.discard(i-j)
        fun(0)
        return res
