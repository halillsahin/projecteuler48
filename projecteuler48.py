a=0
for i in range(1,1001):
    a+=(i**i)
print(str(a)[len(str(a))-10::])
