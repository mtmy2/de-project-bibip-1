'''
with open("D:\\YandexDisk\\Документы\\Обучение\\DataAnalisys\\Яндекс практикум\\YaMyPract\\de-project-bibip\\de-project-bibip\\src\\sales_index.txt", 'r+') as si:
    line_number = si.readlines()
    print(line_number)
'''

# Задание 2. Сохранение продаж.
# запись в файл sales.txt
#def sell_car():
with open("D:\\YandexDisk\\Документы\\Обучение\\DataAnalisys\\Яндекс практикум\\YaMyPract\\de-project-bibip\\de-project-bibip\\src\\sales.txt", 'a') as sales:
    sales.write(f'1,"aaa111","01/01/2025",100'.ljust(500)+'\n')

# Запись в файл sales_index.txt
with open("D:\\YandexDisk\\Документы\\Обучение\\DataAnalisys\\Яндекс практикум\\YaMyPract\\de-project-bibip\\de-project-bibip\\src\\sales_index.txt", 'w+') as si:
    readlines=si.readlines()
    line_number = len(readlines)
    #line_number = len(si.readlines())+1
    if line_number == 0:
        readlines = [f'"aaa222",{line_number+1}'+'\n']
    else:
        readlines.append(f'aaa222,{line_number+1}'+'\n')
    sales_index_sorted = sorted(readlines)
with open("D:\\YandexDisk\\Документы\\Обучение\\DataAnalisys\\Яндекс практикум\\YaMyPract\\de-project-bibip\\de-project-bibip\\src\\sales_index.txt", 'w+') as si:
    for line in sales_index_sorted:
        si.write(f'{line}')

# получение номера строки с нужным vin из car_index
cars_line=0
with open("D:\\YandexDisk\\Документы\\Обучение\\DataAnalisys\\Яндекс практикум\\YaMyPract\\de-project-bibip\\de-project-bibip\\src\\cars_index.txt", 'r+') as ci:
    cars_index_lines = ci.readlines()
    for line in cars_index_lines:
        current_index_line = line.strip().split(',')
        vin = current_index_line[0]
        current_cars_line = current_index_line[1]
        if vin == "aaa222":
            cars_line = int(current_cars_line)
            

# получение строки с нужным vin из car
with open("D:\\YandexDisk\\Документы\\Обучение\\DataAnalisys\\Яндекс практикум\\YaMyPract\\de-project-bibip\\de-project-bibip\\src\\cars.txt", 'r+') as cars:
    lines = cars.readlines()
    current_car_info_raw = lines[cars_line-1]
    current_car_info = current_car_info_raw.strip().split(',')
# запись статуса в нужный список
    current_car_info[4] = 'sold'
# преобразование списка в строку и запись в файл
    new_car_line = f'{current_car_info[0]},{current_car_info[1]},{current_car_info[2]},{current_car_info[3]},{current_car_info[4]}'.ljust(500)+'\n'
    cars.seek((cars_line-1) * (501))
    cars.write(new_car_line)
