

class ContainDuplicates(object):

# where n is the number of elements in the array
# O(n^2) || O(1)
    def containDuplicateBruteForce(self, array):
        if not array: return False

        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] == array[j]:
                    return True

        return False

# where n is the number of elements in the array
# O(n) || O(n) 
    def containDuplicateWithSet(self, array):
        if not array: return False

        hashSet = set()
        for i in array: 
            if i in hashSet:
                return True
            hashSet.add(i)

        return False
        
        # OR

        return len(set(array)) == len(array)


# O(nlogn) || O(1)
    def containDuplicateWithSorting(self, array):
        if not array: return False
        array.sort()
        for i in range(1, len(array)):
            if array[i-1] == array[i]:
                return True

        return False

    




l = [1, 2, 3, 1]

print(ContainDuplicates().containDuplicateBruteForce(l))
print(ContainDuplicates().containDuplicateWithSet(l))
print(ContainDuplicates().containDuplicateWithSorting(l))