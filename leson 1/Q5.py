proceeds = float(input("Enter proceeds: "))
costs = float(input("Enter costs: "))

if proceeds > costs:
    print('Good Job')
    income = proceeds - costs
    print('Profitability of firm {:%}'.format(income / proceeds))
    employees = int(input('Employees string: '))
    print(f'Profitability of employ {income / employees} $')
else:
    print('Bad Job')
