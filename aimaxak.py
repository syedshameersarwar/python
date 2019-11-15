donut_condition = ''
score = 20
donut_price = ''
donut_filling = ''
if donut_condition == 'fresh':
    score += 10
if donut_filling == 'chocolate':
    score += 5
if donut_price == 'reasonable':
    score += 7

print('Buy Score:',score)
