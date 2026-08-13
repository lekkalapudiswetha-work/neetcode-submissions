class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board),len(board[0])
        safe = [[False] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols-1) and board[r][c] == 'O':
                    safe[r][c] = True
                    queue.append((r,c))
        
        directions = [
            [1,0],[-1,0],[0,1],[0,-1]
        ]
        # print(safe)
        
        while queue:
            r,c = queue.popleft()
            
            for dr , dc in directions:
                nr = r+dr
                nc = c+dc
                if 0 <= nr <rows and 0 <= nc <cols and board[nr][nc] == 'O' and not safe[nr][nc]:
                    safe[nr][nc] = True
                    queue.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and not safe[r][c]:
                    board[r][c] = 'X'

        