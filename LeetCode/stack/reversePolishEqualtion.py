def evalRPN(tokens):
    stack = []
    
    for num in tokens:
        if num in {'+', '-', '/', '*'}:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(makeEquation(num1, num2, num))
        else:
            stack.append(int(num))
    
    return stack[len(stack)-1]

def makeEquation(num1, num2, symbol):
    equation = {
        '+' :    num1 + num2,
        '-' :    num2 - num1,
        '*' :    num1 * num2,
        }
    if not symbol in equation:
        return int(num2 / num1)
    return equation[symbol]



print(evalRPN(["2","1","+","3","*"]))