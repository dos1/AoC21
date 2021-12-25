l,R,L=[[a for a in line.strip()] for line in open("inputday25")],range,len;w,m,i=lambda x,y:((x,0)[x>=L(l[0])],(y,0)[y>=L(l)]),1,0;d=l
def M(d,o,a,b,c,m=0):
 for x,y in((x,y)for x in R(L(d[0]))for y in R(L(d))):i,j=w(x+a,y+b);v=(o[y][x]==c)*(o[j][i]=='.');d[y][x],d[j][i]=((d[y][x],d[j][i]),('.',c))[v];m|=v
 return m
while m:m,o,d=0,d,[[*x]for x in d];m|=M(d,o,1,0,'>')+M(d,[[*x]for x in d],0,1,'v');i+=1
print(i)
