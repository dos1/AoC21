def I(d,idx,val):d[idx]=d.setdefault(idx,0)+val
L=open("inputday14").readlines();t,d,p=L[0],dict([l.strip().split(' -> ')for l in L[2:]]),{};[I(p,t[i:i+2],1)for i in range(len(t)-2)]
def E(P):o=dict(P);[(I(P,p,-o[p]),I(P,p[0]+n,o[p]),I(P,n+p[1],o[p]))for p,n in d.items()if p in o.keys()];return P
def C(P):e={};[I(e,c,v)for p,v in P.items()for c in p];return{x:-int(e[x]/2//-1)for x in e}
print((r:=[max(e:=C(E(p)).values())-min(e)for i in range(40)])[9],r[-1])
