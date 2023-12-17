high_risk_returns = {}
medium_risk_returns = {}
low_risk_returns = {}

amount = 1
key = -501000
for i in range(-1000, 1001):
    temp_amount = amount
    while temp_amount > 0:
        high_risk_returns[key] = i / 100.0
        temp_amount -= 1
        key += 1
    if key < 0:
        amount += 1
    else:
        amount -= 1

amount = 1
key = -125500
for i in range(-500, 501):
    temp_amount = amount
    while temp_amount > 0:
        medium_risk_returns[key] = i / 100.0
        temp_amount -= 1
        key += 1
    if key < 0:
        amount += 1
    else:
        amount -= 1

amount = 1
key = -20200
for i in range(-200, 201):
    temp_amount = amount
    while temp_amount > 0:
        low_risk_returns[key] = i / 100.0
        temp_amount -= 1
        key += 1
    if key < 0:
        amount += 1
    else:
        amount -= 1