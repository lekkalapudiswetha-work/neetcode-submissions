class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = [[False] * n for _ in range(n)]
        result = []

        def checkDiagonal(i,j):
            r, c = i - 1, j - 1
            while r >= 0 and c>= 0:
                if visited[r][c]:
                    return False
                r-=1
                c-=1
            r, c = i - 1, j + 1
            while r >= 0 and c < n:
                if visited[r][c]:
                    return False
                r-=1
                c+=1
            return True
        
        def columnCheck(i,j):
            while i >= 0:
                if visited[i][j]:
                    return False
                i-=1
            return True

        def backtrack(i,curr):
            if i == n:
                if len(curr) == n:
                    result.append(curr.copy())
                return
            
            for j in range(n):
                if checkDiagonal(i,j) and columnCheck(i,j):
                    visited[i][j] = True
                    row = ['.'] * n
                    row[j] = 'Q'
                    curr.append(''.join(row))
                    backtrack(i+1,curr)
                    visited[i][j] = False
                    curr.pop()
        
        backtrack(0,[])
        return result


    