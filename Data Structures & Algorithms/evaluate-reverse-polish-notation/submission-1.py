class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for c in tokens:
            if c not in ["+", "-", "*", "/"]:
                stk.append(int(c))
            else:
                second = stk.pop()
                first = stk.pop()
                #compute = operand(first, second)
                if c == '+':
                    compute = first + second
                elif c == '-':
                    compute = first - second
                elif c == '*':
                    compute = first * second
                else:
                    compute = int(first / second)
                stk.append(compute)
        return stk[-1]
            