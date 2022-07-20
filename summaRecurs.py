def sum(arr):
    if len(arr) == 1:
        return 0
    else:
        x = 0
        x += arr[0]
        sum(arr.pop(0))
        return x

         


    
    
    
    



spam = [2, 4, 6]

print(sum(spam))
