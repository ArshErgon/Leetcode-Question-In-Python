

class ReverseString:


    def reverseStringWithNewList(self, string):
        if not string:
            return string

        newList = [0] * len(string)

        j = 0
        for i in reversed(range(len(string))):
            newList[i] = string[j]
            j += 1

        return newList


    def reverseStringOptimal(self, string):
        if not string: return string
        left, right = 0, len(string) - 1

        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

        return string


    def reverseStringWithListCompression(self, string):
        if not string: return string
        return [string[i] for i in reversed(range(len(string)))]

    
    def reversedStringWithReverse(self, string):
        string.reverse() 
        return string or string[::-1]




sol = ReverseString()
print(sol.reverseStringWithNewList(["H","a","n","n","a","h"]))
print(sol.reverseStringOptimal(["h","e", "l", "l", "o"]))
print(sol.reverseStringWithListCompression(["H","a","n","n","a","h"]))
print(sol.reversedStringWithReverse(["H","a","n","n","a","h"]))
