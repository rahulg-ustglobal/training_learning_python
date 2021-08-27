class employee:
    no_of_leaves=8
    def __init__(self,name,salary,profile):
        self.name=name
        self.salary=salary
        self.profile=profile

obj1=employee("Rahul",2024,"Engineer")
print(obj1.salary)
print(obj1.name)
print(obj1.profile)

