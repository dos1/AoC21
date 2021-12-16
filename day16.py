d="".join(["0"*(4-len(b:=bin(int(i,16))[2:]))+b for i in open("inputday16").read().strip()])
consume=lambda d,n:(d[:n],d[n:]);intval=lambda d,n:(int((D:=consume(d,n))[0],2),D[1])
def mul(v):
 p=1
 for i in v:p*=i
 return p
def parse(d):
 ver,d=intval(d,3);typeID,d=intval(d,3)
 if typeID==4:
  number="";prefix,d=intval(d,1)
  while prefix:num,d=consume(d,4);number+=num;prefix,d=intval(d,1)
  num,d=consume(d,4);number+=num
  return int(number,2),ver,d
 op=[sum,mul,min,max,4,lambda x:x[0]>x[1],lambda x:x[0]<x[1],lambda x:x[0]==x[1]][typeID]
 subvalues=[];lengthType,d=intval(d,1)
 if lengthType:
  length,d=intval(d,11)
  for i in range(length):val,subsum,d=parse(d);subvalues+=[val];ver+=subsum
 else:
  length,d=intval(d,15);sub,d=consume(d,length)
  while len(sub) and int(sub,2):val,subsum,sub=parse(sub);subvalues+=[val];ver+=subsum
 return op(subvalues),ver,d
print((x:=parse(d))[1],x[0])
