def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    
    # Traverse the array from right to left
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    # Leaders were added in reverse order, so reverse the list
    leaders.reverse()
    return leaders


# Example
arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", findLeaders(arr))
