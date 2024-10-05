list = [56,34,1,4,76]
print("This list is incorrectly sorted.",list)

for i in range(0,len(list)):
    for j in range(i,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]#this is how they get swapped
print(" This is the correct order:", list)