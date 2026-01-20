class Solution:
    def solveEquation(self, equation: str) -> str:

        def parse(exp):
            coef = 0
            const = 0
            i = 0
            sign = 1
            
            while i < len(exp):
                if exp[i] == '+':
                    sign = 1
                    i += 1
                elif exp[i] == '-':
                    sign = -1
                    i += 1
                else:
                    num = 0
                    isNumber = False
                    
                    while i < len(exp) and exp[i].isdigit():
                        num = num * 10 + int(exp[i])
                        i += 1
                        isNumber = True
                    
                    if i < len(exp) and exp[i] == 'x':
                        # coefficient of x
                        if isNumber:
                            coef += sign * num
                        else:
                            coef += sign * 1
                        i += 1
                    else:
                        # constant
                        const += sign * num
            
            return coef, const
        
        left, right = equation.split('=')
        lcoef, lconst = parse(left)
        rcoef, rconst = parse(right)
        
        # merging
        xcoef = lcoef - rcoef       # move x terms to left
        c = rconst - lconst         # move const terms to right
        
        if xcoef == 0:
            if c == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        return "x=" + str(c // xcoef)
