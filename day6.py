F,C=[int(val)-8 for val in open("inputday6").read().split(',')],lambda f,d,D:[(n,(D[f],1)[f<0])for n in range(9+f,d,7)]
def count(D):
  for f in F+list(range(len(D))):
    for n,a in C(f,len(D),D):D[n]+=a
  return len(F)+sum(D)
print(*(count([0]*(d+1))for d in(80,256)))
