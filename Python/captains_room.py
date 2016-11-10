K,r = int(input()), list(map(int,input().split()))
s = set(r)
print(((sum(s)*K)-(sum(r)))//(K-1))

#Method
#K = n
#r = {a, bn, cn, dn, ... zn}
#s = set(r) = {a, b, c, d, .... z}
#sum(s) * K = sum(n{a,b,c,d,....z})
#sum(r) = sum({a, bn, cn, dn, ... zn})
#sum(s)*K - sum(r) = (n-1)*a
#K-1 = n -1; so (sum(s)*K - sum(r)) / (K-1) = a

#this method timed out
#for i in r:
#    if r.count(i) != K:
#        print(i)