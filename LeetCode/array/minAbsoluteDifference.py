

# O(nlogn) || O(n)
from collections import defaultdict
def minimumAbsDifference(arr):
    arr.sort()
    hashMap = defaultdict(list)

    minDifference = float('inf')
    for i in range(0, len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        hashMap[diff].append([arr[i], arr[i + 1]])
        minDifference = min(minDifference, diff)

    
    return hashMap[minDifference]


# arr = [4,2,1,3]
arr = [1,3,6,10,15]
# arr = [3,8,-10,23,19,-4,-14,27]
arr = [40,11,26,27,-20]

print(minimumAbsDifference(arr))