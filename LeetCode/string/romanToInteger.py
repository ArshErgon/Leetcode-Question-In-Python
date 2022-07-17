

def romanToInteger(stringNum):
    romanMap = {
        'I' :     1,
        'V' :     5,
        'X' :     10,
        'L' :     50,
        'C' :     100,
        'D' :     500,
        'M' :     1000,
    } 

    totalNum = 0
    for i in reversed(range(len(stringNum))):
        roman = romanMap[stringNum[i]]
        if 4 * roman < totalNum:
            totalNum -= roman
        else:
            totalNum += roman
    return totalNum
    
num = 'MCMXCIV'

print(romanToInteger(num))