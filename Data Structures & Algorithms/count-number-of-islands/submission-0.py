class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0

        def visitLands(grid, row, column, path):
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] == "0" or (row, column) in path:
                return
            else:
                path.add((row, column))
                visitLands(grid, row + 1, column, path)
                visitLands(grid, row - 1, column, path)
                visitLands(grid, row, column + 1, path)
                visitLands(grid, row, column - 1, path)

            return path

        def combined(grid):
            path = set()

            for row in range(len(grid)):
                for column in range(len(grid[0])):
                    if (row, column) not in path and grid[row][column] == "1":
                        self.count += 1
                        visitLands(grid, row, column, path)

        combined(grid)
        return self.count