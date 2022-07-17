




def asteriodCollision(asteriods):
    stack = []
    for asteriod in asteriods:
        
        while stack and asteriod < 0 < stack[-1]:
            diff = asteriod + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                asteriod = 0
            else:
                asteriod = 0
                stack.pop()
        if asteriod != 0:
            stack.append(asteriod)
    return stack

print(asteriodCollision([5,10,-5]))
print(asteriodCollision([8, -8]))
print(asteriodCollision([10,2,-5]))
print(asteriodCollision([-1,3,2,-3]))
print(asteriodCollision([-2,-1,1,2]))