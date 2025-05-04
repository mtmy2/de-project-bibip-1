with open('/sales_index.txt', 'r+') as si:
    line_number = len(si.read().split('\n'))
    print(line_number)