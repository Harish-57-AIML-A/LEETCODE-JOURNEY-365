class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix: return []
        elements = []
        m, n = len(matrix), len(matrix[0])
        row, col = 0, -1
        
        while True:
            for _ in range(n):
                col += 1
                elements.append(matrix[row][col])
            m -= 1
            if m == 0: break
            
            for _ in range(m):
                row += 1
                elements.append(matrix[row][col])
            n -= 1
            if n == 0: break
            
            for _ in range(n):
                col -= 1
                elements.append(matrix[row][col])
            m -= 1
            if m == 0: break
            
            for _ in range(m):
                row -= 1
                elements.append(matrix[row][col])
            n -= 1
            if n == 0: break
        
        return elements
