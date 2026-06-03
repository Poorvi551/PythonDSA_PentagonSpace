def linear_search(col,key):
    for i in range(len(col)):
        if col[i]==key:
            return i
    return -1
col=eval(input("Enter list:"))
key=int(input("Enter key val:"))
print(linear_search(col,key))