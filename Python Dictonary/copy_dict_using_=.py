original={
    'One':1,
    'Two':2,
    'Three':3,
    'Four':4,
    'Five':5
}
print("Copy Dict By using equals operator:=")
new=original
print("New Dict:=",new)
print("Original Dict:=",original)
print("Copy Dict By using copy() Method:=")
x=original.copy()
original.clear()
print("Copy Dict by using copy() method:=",x)
print("After the clear original Dict:=",original)
print("After the clear original Dict the copied Dict:=",x)


