#First way
dict1={"a":1 , "b":2 , "c":3}
dict2={"d":4 , "e":5 , "f":6}

dict2.update(dict1)
print(dict2)

#Second way
dict3={**dict1,**dict2}
print(dict3)

#Third way
dict4=dict(dict1.items() | dict2.items())
print(dict4)
