def calculation(n):
    return n*n
numbers=(1,2,3,4,5)
ans=map(calculation,numbers)

print(ans)

num=set(ans)
print(num)