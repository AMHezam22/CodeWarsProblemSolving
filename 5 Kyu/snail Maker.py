# https://www.codewars.com/kata/536a155256eb459b8700077e/train/python

def create_spiral(n):
	if not type(n) == int or n <= 0:
		return []
	ans = [[None] * n for _ in range(n)]
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	dirIdx = 0
	c, r = 0, 0
	for x in range(1, n * n + 1):
		ans[r][c] = x
		nr, nc = r + directions[dirIdx][0], c + directions[dirIdx][1]
		if nr < 0 or nr >= n or nc < 0 or nc >= n or ans[nr][nc] is not None:
			dirIdx = (dirIdx + 1) % 4
			nr, nc = r + directions[dirIdx][0], c + directions[dirIdx][1]
		r, c = nr, nc
	return ans


s = create_spiral("5")
print(s)
