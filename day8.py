L,R=[[[*map(set,a.split())]for a in l.split('|')]for l in open("inputday8")],{2:1,3:7,4:4,7:8}
def C(l):
 *d,=map(len,l);S,X,z=[0]*10,lambda L:[a for a in l if len(a)==L],lambda a,b:a&b==a
 for i in R.keys():S[R[i]]=l[d.index(i)]
 for e in X(6):S[[[6,0][z(S[1],e)],9][z(S[4],e)]]=e
 for e in X(5):S[[[2,5][z(e,S[6])],3][z(S[1],e)]]=e
 return S
print(sum([*"".join(o:=["".join(str(C(l).index(a))for a in w)for l,w in L])].count(str(i))for i in R),sum(map(int,o)))
