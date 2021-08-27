l1=[]
l2=[]
n1=int(input("how many elements you want to add in L1:="))
print("Enter the elements of L1:=")
for i in range(0,n1):
    ele1=int(input())
    l1.append(ele1)
n2=int(input("how many elements you want to add in L2:="))
print("Enter the elements of L2:=")
for j in range(0,n2):
    ele2=int(input())
    l2.append(ele2)
print(l1)
print(l2)
x=list(map(lambda l,m : l*m,l1,l2))
print("This is map:=",x)
x1=list(filter(lambda s : s%2!=0,range(0,len(l1))))
print("This is filter to find odd numbers:=",x1)