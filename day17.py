X,Y=map(lambda x:[*map(int,x.split('..'))],open("inputday17").readline().strip()[15:].split(', y='))
# we're assuming that target area's X values are always positive and Y values are always negative ¯\_(ツ)_/¯
def C(x,y):
 V=((Z:=lambda x:(0,x-1)[x>0])(x),y-1)
 while x<=X[1]and y>=Y[0]:
  if x>=X[0]and y<=Y[1]:return 1
  x+=V[0];y+=V[1];V=(Z(V[0]),V[1]-1)
 return 0
print((h:=max((c:=[i for i in[[y for y in range(Y[0],-Y[0])if C(x,y)]for x in range(X[1]+1)]if i])[0]))*(h+1)//2,sum(map(len,c)))
