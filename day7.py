*F,=map(int,[*open("inputday7")][0].split(','))
print(*(min(sum(c(abs(a-i))for i in F)for a in range(max(F)+1))for c in[lambda i:i,lambda i:i*(i+1)//2]))
