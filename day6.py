N,F=257,[int(f)-8 for f in[*open("inputday6")][0].split(',')];D=[0]*N
print(*[D.__setitem__(n,D[n]+(D[f],1)[f<0])for f in F+[*range(N)]for n in range(9+f,N,7)]and(len(F)+sum(D[:x])for x in(81,N)))
