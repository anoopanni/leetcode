arr = [1, 3, 5, 10, 12, 16, 100, 200]

def binary_search(l, r, target):
    
    while l <= r:
        mid = (l + r) // 2
        
        if arr[mid] <= target:   # Equals = Right fit and Not Equals means left fit
            l = mid + 1
        else:
            r = mid - 1
            
    print(arr[l])
        
# (left fit, right fit) answers below :

binary_search(0, len(arr) - 1, 16)  # (16, 100) 
