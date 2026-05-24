class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        self.currentArea = 0

        def initialize_currentArea():
            self.currentArea = 0

        def measureArea(grid, row, column, path):
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] == 0 or (row,column) in path:
                return 
            else:
                self.currentArea += 1
                path.add((row, column))
                measureArea(grid, row + 1, column, path)
                measureArea(grid, row - 1, column, path)
                measureArea(grid, row, column + 1, path)
                measureArea(grid, row, column - 1, path)

        
        def combined(grid):
            path = set()

            for row in range(len(grid)):
                for column in range(len(grid[0])):
                    if grid[row][column] == 1 and (row, column) not in path:
                        initialize_currentArea()
                        measureArea(grid, row, column, path)

                        if self.currentArea > self.maxArea:
                            self.maxArea = self.currentArea


        combined(grid)
        return self.maxArea

