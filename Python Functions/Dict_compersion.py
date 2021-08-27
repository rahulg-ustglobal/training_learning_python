#1)First way of Dict
dic=dict()
for num in range(1,11):
    dic[num]=num*num
print(dic)

#2)Second way of Dict
dicts={num:num*num for num in range(1,11)}
print(dicts)