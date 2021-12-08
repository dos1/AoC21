L=[[[*map(sorted,a.split())]for a in l.split('|')]for l in open("inputday8")]
z=lambda a,b:len([c for c in a if c in b])==len(a)
def C(l):
 *d,=map(len,l);S=[0]*10;X=lambda L:[a for a in l if len(a)==L]
 for i in(a:={2:1,3:7,4:4,7:8}).keys():S[a[i]]=l[d.index(i)]
 for e in X(6):S[9 if z(S[4],e)else 0 if z(S[1],e)else 6]=e
 for e in X(5):S[3 if z(S[1],e)else 5 if z(e,S[6])else 2]=e
 return S
print(sum([int("".join([str(C(l).index(a))for a in w]))for l,w in L]))
