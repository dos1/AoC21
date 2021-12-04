lines=[line.strip() for line in open("inputday3").readlines()]
LEN=len(lines[0])

def bintoint(s):
  return sum(2**((len(s)-1)-i) for i,c in enumerate(s) if c == '1')

def algo(l, rule):
  for i in range(LEN):
    l = [line for line in l if line[i] == rule(sum([int(line[i]) for line in l]),l)]
    if len(l) == 1:
      break
  return l[0]

zeros = [0]*LEN
ones  = [0]*LEN
for line in lines:
  for i,c in enumerate(line):
    ones[i] += c == '1'
    zeros[i] += c == '0'
gamma   = [('0' if zero > one else '1') for zero,one in zip(zeros,ones)]
epsilon = [('1' if zero > one else '0') for zero,one in zip(zeros,ones)]
oxygen = algo(lines, lambda s,l: '1' if s >= len(l) / 2 else '0')
co2    = algo(lines, lambda s,l: '1' if s <  len(l) / 2 else '0')

print(bintoint(gamma) * bintoint(epsilon), bintoint(oxygen) * bintoint(co2))
