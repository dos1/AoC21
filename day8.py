L,z=[[[*map(set,a.split())]for a in l.split('|')]for l in open("inputday8")],lambda a,b:a&b==a
def C(l):
 *d,=map(len,l);S=[0]*10;X=lambda L:[a for a in l if len(a)==L]
 for i in(a:={2:1,3:7,4:4,7:8}).keys():S[a[i]]=l[d.index(i)]
 for e in X(6):S[[[6,0][z(S[1],e)],9][z(S[4],e)]]=e
 for e in X(5):S[[[2,5][z(e,S[6])],3][z(S[1],e)]]=e
 return S
print(sum([*"".join(o:=["".join([str(C(l).index(a))for a in w])for l,w in L])].count(str(i))for i in(1,4,7,8)),sum(map(int,o)))
