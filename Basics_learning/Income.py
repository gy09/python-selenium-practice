def net_income(state, income):
    """will calculate the net income after tax deduction"""

    if state == 'NYC':
        net_value = ((income)-((income*.10)+(income*.12)))
        return net_value
    elif state == 'CA':
        net_value = ((income) - ((income * .10) + (income * .11)))
        return net_value
    elif state == 'MO':
        net_value = ((income) - ((income * .10) + (income * .14)))
        return net_value
    else:
        net_value = ((income) - ((income * .10) + (income * .15)))
        return net_value


net_income_value = net_income('NYC', 100000)
print(net_income_value)


