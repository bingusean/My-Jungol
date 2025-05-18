grid = [[0 for _ in range(5)] for _ in range(5)]

grid[0][0] = 1
grid[0][2] = 1
grid[0][4] = 1

for r in range(1, 5):
    for c in range(5):
        left = grid[r - 1][c - 1] if c - 1 >= 0 else 0
        right = grid[r - 1][c + 1] if c + 1 < 5 else 0
        grid[r][c] = left + right

for row in range(5):
    for col in range(5):
        print(grid[row][col], end=' ')
    print("")