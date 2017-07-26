#National Average kWh cost
kwh_cost = 12.56
time_hours = 0

#Find out how many watts
kwh_v = float(input('How many volts? '))
kwh_a = float(input('How many amperes? '))
kwh_w = float(kwh_v * kwh_a)
print('..', kwh_w, 'watts\n')

#Find out how many weeks grow cycle
time_weeks = int(input('How many weeks? '))
kwh = float(kwh_w * int(time_weeks * 7 * 24) / 1000)

#time_hours = int(time_weeks * 7 * 24)
#kwh = float(kwh_w * time_hours / 1000)

#Output information
print('..', time_weeks,'  weeks.')
print('..', (time_weeks * 7 * 24),'  hrs.')
print('..', kwh,'kWh.\n')
print('The national average for Residential energy rates is $12.56/kwh')
print('$', kwh * kwh_cost,' per grow cycle.\n\n')
