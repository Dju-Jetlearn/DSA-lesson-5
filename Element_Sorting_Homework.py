list = [1,2,3,4,76,165,34,132,85,21]
print("This list is incorrectly sorted.",list)

for i in range(0,len(list)):
    for j in range(i,len(list)):
        if list[i] < list[j]:
            list[i],list[j] = list[j],list[i]
print(" This is the correct order:", list)