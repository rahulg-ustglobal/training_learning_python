import datetime

x=datetime.datetime.now()
print(x.time())
print(x.strftime("%A"))

"""
y=time.time()
print(y)
print("--- %s seconds ---" % (time.time() - y))
"""