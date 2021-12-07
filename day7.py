*F,=map(int,[*open("inputday7")][0].split(','));C={i:F.count(i)for i in F}
print(*(min(sum(c(abs(a-i))*C[i]for i in C)for a in range(max(F)+1))for c in[lambda i:i,lambda i:sum(range(i+1))]))
