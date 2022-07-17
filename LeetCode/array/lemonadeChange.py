

# O(n) || O(1)
def lemonadeChange(bills):
    fiveBills, tenBills = 0, 0

    for i in bills:
        if i == 5:
            fiveBills += 1
        elif i == 10:
            fiveBills -= 1
            tenBills += 1
        elif tenBills > 0:
            fiveBills -= 1
            tenBills -= 1
        else:
            fiveBills -= 3

        if fiveBills < 0:
            return False


    return True  
        


print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([5,5,10,10,20]))
print(lemonadeChange([5,5,5,10,5,5,10,20,20,20]))


