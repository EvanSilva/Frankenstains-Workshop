def fi(arr, n):
        smallList = arr[:]
        while len(smallList) > n:
            smallNumber = max(smallList)
            smallList.remove(smallNumber)
            
        return smallList




def first_n_smallest(arr, n):
        smallList = arr[:]
        while len(smallList) > n:
            maxNumber = max(smallList)
            smallList.reverse()
            smallList.remove(maxNumber)
            smallList.reverse()
                  
            
        return smallList

print(first_n_smallest([1,2,3,1,2],3))
