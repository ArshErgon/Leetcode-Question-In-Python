


class HouseRobber:
    def houseRobber(self, array):
        if not array:
            return 0

        rob1, rob2 = 0, 0
        for i in array:
            temp = max(i + rob1 , rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


print(HouseRobber().houseRobber([1,2,3,1]))