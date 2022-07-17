

class MoveZero(object):

# O(n) || O(1) space: but its a bad practice;
# appending a element is an O(1) operation but when you pop(O(1)) 
# all the elements to its right move to fill the space. O(n)

    def moveZero1(self, nums):
        if not nums:return nums
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

        return nums


    def moveZero2(self, nums):
        if not nums:
            return nums

        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)

        return nums


    def moveZero3(self, nums):
        if not nums:return nums

        nextPtr = 0

        for num in nums:
            if num != 0:
                nums[nextPtr] = num
                nextPtr += 1
        
        for i in range(nextPtr, len(nums)):
            nums[i] = 0

        return nums


    def moveZero4(self, nums):
        if not nums:return nums

        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
    



l = [0, 0, 1]
sol = MoveZero()

# print(sol.moveZero1(l))
print(sol.moveZero4(l))
        