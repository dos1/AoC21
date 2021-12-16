d=bin(int(x:=open("inputday16").read()[:-1],16))[2:].zfill(len(x)*4)
C,I=lambda d,n:(d[:n],d[n:]),lambda d,n:(int((D:=C(d,n))[0],2),D[1])
def m(v):
 p=1
 for i in v:p*=i
 return p
def P(d):
 v,d=I(d,3);t,d=I(d,3)
 if t==4:
  n,p="",1
  while p:p,d=I(d,1);N,d=C(d,4);n+=N
  return int(n,2),v,d
 S=[];L,d=I(d,1)
 if L:
  l,d=I(d,11)
  for i in range(l):V,Z,d=P(d);S+=[V];v+=Z
 else:
  l,d=I(d,15);s,d=C(d,l)
  while s:V,Z,s=P(s);S+=[V];v+=Z
 return[sum,m,min,max,4,lambda x:x[0]>x[1],lambda x:x[0]<x[1],lambda x:x[0]==x[1]][t](S),v,d
print((x:=P(d))[1],x[0])
