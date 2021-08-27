l=[]
n=int(input("How many elements you want to add:="))
print("Enter the elements in the list:=")
for i in range(0,n):
    list_eles=int(input())
    l.append(list_eles,)
print(l)
def normal_function(s):
    return s*s
x=list(map(normal_function,l))
print(x)