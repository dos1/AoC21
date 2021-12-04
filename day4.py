with open("inputday4") as f:
  numbers = f.readline().strip().split(',')
  boards = [[[(x, False) for x in line.split()] for line in board.split('\n')] for board in f.read().strip().split('\n\n')]
results = []
for number in numbers:
  boards = [[[(num[0], num[1] or num[0] == number) for num in line] for line in b] for b in boards]
  check = lambda b: True in [False not in [b[i][j][1] for j in range(5)] or False not in [b[j][i][1] for j in range(5)] for i in range(5)]
  results.extend([sum([int(num[0]) for line in b for num in line if not num[1]]) * int(number) for b in filter(check, boards)])
  boards = filter(lambda x: not check(x), boards)
print(results[0], results[-1])
