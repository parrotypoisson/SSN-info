import csv

order = ['group_number']

for x in range(1, 10, 2): order.append(x)
for x in range(10, 99, 2): order.append(x)
for x in range(2, 10, 2): order.append(x)
for x in range(11, 100, 2): order.append(x)

with open('group_number_order.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\n')
    writer.writerow(order)