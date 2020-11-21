def get_max(num1, num2):
    return [0, num1, num2][int((num1-num2)/abs(num2-num1))]