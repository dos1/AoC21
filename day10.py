D,B,s=dict(zip(C:='-)]}>',(0,3,57,1197,25137))),'\n([{<',0
i=[X for l in open("inputday10")if(X:=(Q:=1,o:=[],W:=[(o.append(C[B.index(c)])if c in B else o.pop()if c==o[-1]else(s:=s+D[c],Q:=0),o)for c in l if Q][-1])[2]and W[1]*Q)]
print(s,sorted((z:=0)or[z:=z*5+C.index(a)for a in reversed(c)][-1]for c in i)[len(i)//2])
