L=[[[*(map(int,v.split(',')))]for v in l.split(' -> ')]for l in open("inputday5")]
ir,m=lambda n,x,y:x<=n<=y or y<=n<=x,max(max(max(p)for p in l)for l in L)+1
ch=lambda a,b,f,s,w:(ir(a,f[0],s[0])and ir(b,f[1],s[1])and(f[0]==s[0]or f[1]==s[1]or(w and abs(f[0]-a)==abs(f[1]-b))))
print(*(sum(a)for a in((sum(ch(i,j,f,s,b)for f,s in L)>1 for j in range(m)for i in range(m))for b in(0,1))))
