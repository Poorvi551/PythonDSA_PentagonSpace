def binary_search(l,key,):
    st=0
    end=len(l)+1
    while st<=end:
        mid = st + end // 2
        if key==l[mid]:
            return mid
        elif key<l[mid]:
            end=mid-1
        else:
            st=mid+1
    return -1
l=eval(input("Enter the sorted collection:"))
key=int(input("Enter the key: "))
print(binary_search(l,key))


