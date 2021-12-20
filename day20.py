A,I=open("inputday20").read().split('\n\n')
I,r,l=[[*l.strip()]for l in I.strip().split('\n')],range,len
g=lambda x,y:I[x][y]if(0<=x<l(I)and 0<=y<l(I[0]))else e
a=lambda x:A[int("".join([['0','1'][c=='#']for c in x]),2)]
E=lambda X,Y:a([g(x,y)for x in r(X-1,X+2)for y in r(Y-1,Y+2)])
p,e=lambda:[[E(a-1,b-1)for b in r(l(I[0])+2)]for a in r(l(I)+2)],'.'
c,C=lambda i:"".join(["".join(x)for x in i]).count('#'),[]
for i in range(50):I,e=p(),a([e]*9);C+=[c(I)]
print(C[1],C[49])
