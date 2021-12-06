F=[int(f)-8 for f in open("inputday6").read().split(',')]
c=lambda D:[D.__setitem__(n,D[n]+a)for f in F+[*range(len(D))]for n,a in((n,(D[f],1)[f<0])for n in range(9+f,len(D),7))]and len(F)+sum(D)
print(c([0]*81),c([0]*257))
