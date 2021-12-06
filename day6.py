F=[int(f)-8 for f in open("inputday6").read().split(',')]
print(*([D.__setitem__(n,D[n]+(D[f],1)[f<0])for f in F+[*range(len(D))]for n in range(9+f,len(D),7)]and len(F)+sum(D)for D in([0]*81,[0]*257)))
