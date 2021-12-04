l=open("inputday1").readlines()

print([sum(int(a)>int(b)for a,b in zip(l[n:],l))for n in(1,3)])
