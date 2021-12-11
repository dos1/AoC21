data=[[*map(int,line.strip())]for line in open("inputday11")]
fields,field=[(i,j)for j in range(len(data[0]))for i in range(len(data))],lambda i,j:data[i][j]
adjacent=lambda i,j:[(a,b)for a in range(i-1,i+2)for b in range(j-1,j+2)if a>=0 and b>=0 and a<len(data)and b<len(data[0])]

def octopus(i, j):
  if data[i][j] > 9:
    data[i][j] = 0
    for a,b in adjacent(i,j):
      if data[a][b]: data[a][b]+=1
      octopus(a, b)

sync = flashes = step = 0
while not sync or step <= 100:
  step += 1
  for i,j in fields: data[i][j] += 1
  for i,j in fields: octopus(i, j)
  if step <= 100: flashes += [field(i,j) for i,j in fields].count(0)
  if sum(map(lambda x:field(*x), fields))==0 and not sync: sync = step

print(flashes, sync)
