l1=[]
l2=[]
n=int(input("how many ekements you want to add:="))
print("Enter the number of elements for List1:=")
for i in range(0,n):
    ele1=int(input())
    l1.append(ele1)
print(l1)
n2=int(input("how many ekements you want to add:="))
print("Enter the number of elements for List2:=")
for i in range(0,n2):
    ele2=int(input())
    l2.append(ele2)
print(l2)
print("Two combined list:=",l1+l2)
print(list(map(lambda a,b:a*b,l1,l2)))