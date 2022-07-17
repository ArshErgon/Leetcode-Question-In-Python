



from collections import Counter as count
def heightChecker(heights):
    countFreq = count(heights)
    i = 0
    removal = 0

    for height in heights:
        while countFreq[i] == 0:
            i += 1
        
        if i != height:
            removal += 1
        
        countFreq[i] -= 1

    return removal
            
heights = [1,1,4,2,1,3]

print(heightChecker(heights))




# O(nlogn) ||O(n)
def heightChecker(array):
    for idx, value in enumerate(sorted(array)):
        if value != array[idx]:
            return False
        
    return True



            