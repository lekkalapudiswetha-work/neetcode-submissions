class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def backtrack(i,j,targetPosition):
            if targetPosition == len(word):
                return True

            if i+1 < rows and not visited[i+1][j] and board[i+1][j] == word[targetPosition]:
                visited[i+1][j] = True
                if backtrack(i+1,j,targetPosition+1):
                    return True
                visited[i+1][j] = False

            if i-1 >= 0 and not visited[i-1][j] and board[i-1][j] == word[targetPosition]:
                visited[i-1][j] = True
                if backtrack(i-1,j,targetPosition+1):
                    return True
                visited[i-1][j] = False

            if j+1 < cols and not visited[i][j+1] and board[i][j+1] == word[targetPosition]:
                visited[i][j+1] = True
                if backtrack(i,j+1,targetPosition+1):
                    return True
                visited[i][j+1] = False
                
            if j-1 >= 0 and not visited[i][j-1] and board[i][j-1] == word[targetPosition]:
                visited[i][j-1] = True
                if backtrack(i,j-1,targetPosition+1):
                    return True
                visited[i][j-1] = False
            
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if backtrack(i,j,1):
                        return True
                    visited[i][j] = False
        return False
