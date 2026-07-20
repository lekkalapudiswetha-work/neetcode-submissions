class Solution:
    def totalNQueens(self, n: int) -> int:
        visited = [[False] * n for _ in range(n)]
        result = 0

        def checkDiagonal(i,j):
            r,c = i-1,j-1
            while r>=0 and c >= 0:
                if visited[r][c]:
                    return False
                r-=1
                c-=1
            r,c = i-1,j+1 
            while r>=0 and c < n:
                if visited[r][c]:
                    return False
                r-=1
                c+=1
            return True      
        
        def checkColumn(i,j):
            while i>=0:
                if visited[i][j]:
                    return False
                i-=1
            return True
        
        def backtrack(i):
            nonlocal result
            if i >= n:
                result+=1
                return
            
            for j in range(n):
                if checkDiagonal(i,j) and checkColumn(i,j):
                    visited[i][j] = True
                    backtrack(i+1)
                    visited[i][j] = False

        backtrack(0)
        return result
        