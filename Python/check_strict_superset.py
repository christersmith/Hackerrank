A = set(input().split())
t = list()
for i in range(int(input())):  
    B = set(input().split())
    if B < A: 
        t.append("True")
    else: t.append("False")
if t.count("True") == len(t):
    print("True")
else: print("False")