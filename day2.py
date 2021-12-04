lines = open("inputday2").readlines()

pos = depth = depth2 = aim = 0
for line in lines:
  (cmd, val) = line.split()
  val = int(val)
  if cmd == 'forward':
    pos += val
    depth2 += aim * val
  elif cmd == 'down':
    depth += val
    aim += val
  elif cmd == 'up':
    depth -= val
    aim -= val
print(pos*depth, pos*depth2)
