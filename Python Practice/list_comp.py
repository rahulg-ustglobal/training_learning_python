ls=[]
n=int(input("how many numbers you want to add:="))
for i in range(0,n):
    el=int(input())
    ls.append(el)
print(ls)
ls=[x for x in ls if x%2==0]
print(ls)