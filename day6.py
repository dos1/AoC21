F=[int(val)-8 for val in open("inputday6").read().split(',')]
def count(D):
  for f in F+list(range(len(D))):
    for n,a in[(n,(D[f],1)[f<0])for n in range(9+f,len(D),7)]:D[n]+=a
  return len(F)+sum(D)
print(*(count([0]*(d+1))for d in(80,256)))
