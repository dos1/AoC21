D,B,s,i=dict(zip(C:='-)]}>',(0,3,57,1197,25137))),'\n([{<',0,[]
for l in open("inputday10"):
 o=[]
 for c in l:
  if c in B:o=[C[B.index(c)],*o]
  elif c==o[0]:o=o[1:]
  else:s+=D[c];break
 else:i+=[o]
print(s,sorted((z:=0)or[z:=z*5+C.index(a)for a in c][-1]for c in i)[len(i)//2])
