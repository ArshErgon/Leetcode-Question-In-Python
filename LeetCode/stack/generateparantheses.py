


def generateParenthesis(n):
        res = []
        
        helperFunctionForParenthesis(n, n, '', res)
        return res
        
    
def helperFunctionForParenthesis(opening, closing, preFix, result):
    if opening > 0:
        openingPreFix  = preFix + '('
        
        helperFunctionForParenthesis(opening - 1, closing, openingPreFix, result)
    
    if closing > opening:
        closingPreFix = preFix + ')'
        helperFunctionForParenthesis(opening, closing - 1, closingPreFix, result)
    
    if closing == 0:
        newString = ''.join(preFix)
        result.append(newString)
    

print(generateParenthesis(3))