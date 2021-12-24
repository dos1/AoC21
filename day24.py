# This was a very ill-specified and frustrating task. This solution should work with other inputs,
# but I can't give any guarantee, as inputs aren't really constrained in any way by the task description.

lines = [line.strip().split() for line in open("inputday24")]
variables = {'w': 0, 'x':0, 'y':0, 'z':0}
ranges = {}

def analyze(lines):
  i = -1
  for line in lines:
    if line[0] == "inp": i+=1
    if line[0] == "add" and line[1] == "x" and line[2] != "z":
      num = int(line[2])
      if num <= 9:
        r1 = 1-num
        r2 = 9-num
        ranges[i] = range(min(r1, r2), max(r1,r2) + 1)

def varOrNum(variables, a):
  if a in variables.keys():
    return variables[a]
  return int(a)

def run(data, lines, variables):
  i = 0
  d = None
  while lines:
    line = lines.pop(0)
    if line[0] == "inp":
      if not data:
        lines = [line] + lines
        break
      i += 1
      d = data.pop(0)
      variables[line[1]] = int(d)
    elif line[0] == "add":
      variables[line[1]] += varOrNum(variables, line[2])
    elif line[0] == "mul":
      variables[line[1]] *= varOrNum(variables, line[2])
    elif line[0] == "div":
      variables[line[1]] //= varOrNum(variables, line[2])
    elif line[0] == "mod":
      variables[line[1]] %= varOrNum(variables, line[2])
    elif line[0] == "eql":
      variables[line[1]] = int(variables[line[1]] == varOrNum(variables, line[2]))
  return lines, variables

results = []

def nextDigit(data, lines, variables, r):
  if not lines:
    if variables['z'] == 0:
      return "".join(map(str,data))
    return False
  res = []
  for i in r:
    lin,var = run([i], lines.copy(), variables.copy())
    d = data + [i]
    if len(d) in ranges:
      if not var['z']%26 in ranges[len(d)]:
        continue
    res = nextDigit(d, lin, var, r)
    if res:
      return res

analyze(lines)
print(nextDigit([], lines, variables, range(9,0,-1)), nextDigit([], lines, variables, range(1,10)))
