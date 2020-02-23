b=eval(input())
d=bin(b)
p=len(d)
a=0
k=0
lst=[]
for i in range(2,p):
    if d[i]=='1':
        a=a+1
        k=1
    else:
        k=0
    if k==0 and a!=0:
        lst.append(a)
        a=0
print(max(lst))
