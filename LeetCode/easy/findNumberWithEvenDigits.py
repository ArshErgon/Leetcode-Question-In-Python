


from math import log10


class EvenDigitsLength:
    
    def solOne(self, numArray):
        if not numArray:
            return 0

        counter = 0
        for x in numArray:    
            counter += 1 if len(str(x)) % 2 == 0 else 0

        return counter


    def solTwo(self, numArray):
        if not numArray:
            return 0

        counter = 0

        for num in numArray:
            counter += 1 if (int(log10(num) + 1)) % 2 == 0 else 0

        return counter


    
    def solThree(self, numArray):
        if not numArray:
            return 0

        counter = 0
        for num in numArray:
            if self.helper(num):
                counter += 1

        return counter

    def helper(self, num):
        count = 0
        
        while num > 0:
            num //= 10
            count += 1

        return count % 2 == 0
            


obj = EvenDigitsLength()
l = [12,345,2,6,7896]

print(obj.solOne(l))
print(obj.solTwo(l))
print(obj.solThree(l))