# WAP to implement bubble sort
def bubble_sort(col):
    for i in range(1,len(col)):
        for j in range(0,len(col)-i):
            if col[j]>col[j+1]:
                col[j],col[j+1]=col[j+1],col[j]
    return col
col=eval(input("Enter collection:"))
print(bubble_sort(col))



