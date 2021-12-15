L,R=[[*map(int,l[:-1])]for l in open("inputday15")],range
def i(L,v,e):
 i=0;v[0]=e[0]+e[1]
 if not L or v<L[-1]:L+=[v];return
 for i in R(len(L)):
  if v>=L[i]:L.insert(i,v);return
def r(L):
 Q,a=[L[0][0]],lambda i,j:[L[a][b]for a,b in((i-1,j),(i,j-1),(i+1,j),(i,j+1))if(a>=0)*(b>=0)*(a<len(L))*(b<len(L[0]))]
 while Q and(e:=Q.pop()):[i(Q,f,e)for f in a(*e[2])if f[0]>e[0]+e[1]]
 return(x:=L[len(L)-1][len(L[0])-1])[0]+x[1]
print(*(r([[[(x:=i+j)and float('inf'),x and(s%10+1 if(s:=L[i][j]+n+N)>9 else s),(i+n*len(L),j+N*len(L[0]))]for N in R(l)for j in R(len(L[0]))]for n in R(l)for i in R(len(L))])for l in(1,5)))
