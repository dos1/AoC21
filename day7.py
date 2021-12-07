*F,=map(int,[*open("inputday7")][0].split(','))
print(*(min(sum((z:=abs(a-i),z*(z+1)//2)[c]for i in F)for a in range(max(F)+1))for c in(0,1)))
