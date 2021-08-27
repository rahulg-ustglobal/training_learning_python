class A:
    def feature1(self):
        print("function of feature 1")
    def feature2(self):
        print("function of feature 2")
class B(A):
    def feature3(self):
        print("function of feature 3")
    def feature4(self):
        print("function of feature 4")
#Object of class A
a1=A()
#Access the functions using object
a1.feature1()
a1.feature2()

#Create the object of class B

b1=B()
b1.feature1()

