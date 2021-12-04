SIZE=5

boards=[]
with open("inputday4") as f:
  numbers=f.readline().strip().split(',')
  f.readline()
  while True:
    boards.append([[(x, False) for x in f.readline().split()] for i in range(SIZE)])
    if not f.readline():
      break

results = []
for number in numbers:
  boards = [[[(num[0], num[1] or num[0] == number) for num in line] for line in b] for b in boards]
  check = lambda b: True in [False not in [b[i][j][1] for j in range(SIZE)] or False not in [b[j][i][1] for j in range(SIZE)] for i in range(SIZE)]
  results.extend([sum([int(num[0]) for line in b for num in line if not num[1]]) * int(number) for b in filter(check, boards)])
  boards = filter(lambda x: not check(x), boards)
print(results[0], results[-1])
