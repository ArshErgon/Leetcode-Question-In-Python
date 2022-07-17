
# O(logn) || O(1)
def nextGreatestLetter(letters, target):
    if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
    low = 0
    high = len(letters)-1
    while low <= high:
        mid = (high+low)//2
        
        if  target >= letters[mid]: # in binary search this would be only greater than
            low = mid+1
        
        if target < letters[mid]:
            high = mid-1
            
    return letters[low]

letters = ["c","f","j"]
target = "c"

print(nextGreatestLetter(letters, target))