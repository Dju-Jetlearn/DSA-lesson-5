list = [34,56,1,4,76]
print("This list is incorrectly sorted.",list)

def isort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1] = temp
isort(list)
print("This is the correct order:",list)