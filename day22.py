L=[(*[[*map(int,c.split('..'))]for c in l],z=="on")for z,l in[(z,[c.split('=')[1]for c in l.split(',')])for z,l in[l.strip().split(' ')for l in open("inputday22")]]]
C=lambda c:[(c[0][1]-c[0][0]+1)*(c[1][1]-c[1][0]+1)*(c[2][1]-c[2][0]+1),0][c[0][0]>c[0][1]or c[1][0]>c[1][1]or c[2][0]>c[2][1]]
I,R=lambda a,b:[(max(a[x][0],b[x][0]),min(a[x][1],b[x][1]))for x in[0,1,2]],[]
for l in L:i=[[*I(c,l),1-c[3]]for c in R if C(I(l,c))];R+=[i,[l,*i]][l[3]]
print(*(sum(C(t(c))*[-1,1][c[3]]for c in R)for t in[lambda x:I(x,[(-50,50)]*3),lambda x:x]))
