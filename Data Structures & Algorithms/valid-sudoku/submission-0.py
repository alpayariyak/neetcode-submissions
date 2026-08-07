from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                if digit == ".":
                    continue
                
                box = (row // 3, col // 3)

                for current, seen in [(row, rows),  (col, cols), (box, boxes)]:
                    if digit in seen[current]:
                        return False
                    else:
                        seen[current].add(digit)
        return True 