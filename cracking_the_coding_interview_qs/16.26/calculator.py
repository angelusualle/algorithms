# O(N) time and space
def calculator(eq):
    while not eq.isnumeric():
        try:
            float(eq)
            break
        except:
            pass
        break_light = False
        for i, x in enumerate(eq):
            if x == '*':
                op1, op2 = get_operands(eq, i)
                replace = str(float(op1) * float(op2))
                eq = eq[0:i - len(op1)] + replace +eq[i + len(op2) + 1:]
                break_light = True
                break
            elif x == '/':
                op1, op2 = get_operands(eq, i)
                replace = str(float(op1) / float(op2))
                eq = eq[0:i - len(op1)] + replace +eq[i + len(op2) + 1:]
                break_light = True
                break
        if break_light:
            continue
        for i, x in enumerate(eq):
            if x == '+':
                op1, op2 = get_operands(eq, i)
                replace = str(float(op1) + float(op2))
                eq = eq[0:i - len(op1)] + replace +eq[i + len(op2) + 1:]
                break
            elif x == '-' and i != 0:
                op1, op2 = get_operands(eq, i)
                replace = str(float(op1) - float(op2))
                eq = eq[0:i - len(op1)] + replace +eq[i + len(op2) + 1:]
                break
    return eq

def get_operands(eq, operator_pos, down= True):
    op1 = []
    op1i = operator_pos - 1
    while op1i >= 0 and (eq[op1i].isnumeric() or eq[op1i] == '.'):
        op1.append(eq[op1i])
        op1i -= 1
    op1 = ''.join(reversed(op1))

    op2 = []
    op2i = operator_pos + 1
    while op2i < len(eq) and (eq[op2i].isnumeric() or eq[op2i] == '.'):
        op2.append(eq[op2i])
        op2i += 1
    op2 = ''.join(op2)
    return op1, op2
