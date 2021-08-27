Employee={
   "Name" : "Rahul",
   "Salary" : 13000,
   "Mobno" : 4562358
}
#Use of items() methods
x=Employee.items()
print("Using items() Method:=",x)

#Use of get() method
y=Employee.get("Name")
print("Using get() Method:=",y)

#Use of pop() method

l=Employee.pop("Salary")
print("Using pop() Method:=",l)

ls={
   "Color":"Red",
   "Height":5,
   "Address":"Latur"
}

ls.update(Employee)
print(ls)

p=ls.values()
print("values of the Dict:=",p)
r=ls.keys()
print("Keys of the Dict:=",r)