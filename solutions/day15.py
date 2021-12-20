# credits t0 https://gist.github.com/joshbduncan/b0548d3021e1ecc673dc8877b6c2b6f6
import heapq
from collections import defaultdict

def load_data():
    grid = []
    with open('solutions/day15_input.txt', 'r') as f:
        for line in f:
            grid.append([int(x) for x in line.strip()])
    return grid


def part_one(grid):
    """
    Iterative function to find the minimum cost to traverse from the
    first cell to the last cell of a matrix
    """

	# `M × N` matrix
    (M, N) = (size_y, size_x)

	# `T[i][j]` maintains the minimum cost to reach cell (i, j) from cell (0, 0)
    T = [[0 for x in range(N)] for y in range(M)]

	# fill the matrix in a bottom-up manner
    for i in range(M):
        for j in range(N):
            T[i][j] = grid[i][j]
            
            if i == 0 and j == 0:
                T[0][0] = 0

			# fill the first row (there is only one way to reach any cell in the
			# first row from its adjacent left cell)
            if i == 0 and j > 0:
                T[0][j] += T[0][j - 1]

			# fill the first column (there is only one way to reach any cell in
			# the first column from its adjacent top cell)
            elif j == 0 and i > 0:
                T[i][0] += T[i - 1][0]

			# fill the rest with the matrix (there are two ways to reach any
			# cell in the rest of the matrix, from its adjacent
			# left cell or adjacent top cell)
            elif i > 0 and j > 0:
                T[i][j] += min(T[i - 1][j], T[i][j - 1])
            
            

	# last cell of `T[][]` stores the minimum cost to reach destination cell
	# (M-1, N-1) from source cell (0, 0)
    return T[M - 1][N - 1]


def part_two():

    rows, cols = size_y * 5, size_x * 5
    costs = defaultdict(int)

    pqueue = [(0, 0, 0)]
    heapq.heapify(pqueue)
    visited = set()
    while len(pqueue) > 0:
        cost, row, col = heapq.heappop(pqueue)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        costs[(row, col)] = cost
        if row == rows - 1 and col == cols - 1:
            break

        for mv_y, mv_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + mv_y
            new_col = col + mv_x
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            new_cost = (
                (
                    data[new_row % size_y][new_col % size_x]
                    + (new_row // size_y)
                    + (new_col // size_x)
                )
                - 1
            ) % 9 + 1
            heapq.heappush(pqueue, (cost + new_cost, new_row, new_col))
    return costs[(rows - 1, cols - 1)]


data = load_data()
size_y, size_x = len(data), len(data[0])
print("Part One:",part_one(data))
print("Part Two:",part_two())

