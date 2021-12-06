F=[int(f)-8 for f in open("inputday6").read().split(',')]
def c(D):
  for f in F+[*range(len(D))]:
    for n,a in((n,(D[f],1)[f<0])for n in range(9+f,len(D),7)):D[n]+=a
  return len(F)+sum(D)
print(c([0]*81),c([0]*257))
