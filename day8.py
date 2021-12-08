L,R=[[[*map(set,a.split())]for a in l.split('|')]for l in open("inputday8")],{2:1,3:7,4:4,7:8}
def C(l):
 X,S=lambda L:[a for a in l if len(a)==L],[0]*10
 for i,j in R.items():S[j]=l[[*map(len,l)].index(i)]
 for e in X(6):S[[[6,0][S[1]&e==S[1]],9][S[4]&e==S[4]]]=e
 for e in X(5):S[[[2,5][e&S[6]==e],3][S[1]&e==S[1]]]=e
 return S
print(sum([*"".join(o:=["".join(str(C(l).index(a))for a in w)for l,w in L])].count(str(i))for i in R),sum(map(int,o)))
