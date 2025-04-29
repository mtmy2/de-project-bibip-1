'''
        # Запись в файл models_index.txt
with open('D:\YandexDisk\Документы\Обучение\DataAnalisys\Яндекс практикум\YaMyPract\de-project-bibip\de-project-bibip\src\models_index.txt', 'w+') as mi:
    line_number = str(len(mi.readlines())+1)
    if mi.readlines() == []:
        model_index_new = [f'"Lada",{line_number}'+'\n']
    else:
        model_index_new = mi.readlines().append(f'"Lada",{line_number}'+'\n')
    models_index_sorted = sorted(model_index_new)
    for line in models_index_sorted:
        mi.write(f'{line}\n')
'''



# Задание 2. Сохранение продаж.
# запись в файл sales.txt
with open('D:\YandexDisk\Документы\Обучение\DataAnalisys\Яндекс практикум\YaMyPract\de-project-bibip\de-project-bibip\src\sales.txt', 'a') as sales:
    sales.write(f'1,"aaa111","01/01/2025",100'.ljust(500)+'\n')

# Запись в файл sales_index.txt
with open('D:\YandexDisk\Документы\Обучение\DataAnalisys\Яндекс практикум\YaMyPract\de-project-bibip\de-project-bibip\src\sales_index.txt', 'r', encoding='utf-8') as si:
    line_number = len(si.read().split('\n'))
    #line_number = len(si.readlines())+1
    if line_number == 0:
        sales_index_new = [f'"aaa111",{line_number}'+'\n']
    else:
        sales_index_new = si.readlines().append(f'"aaa111",{line_number}'+'\n')
    sales_index_sorted = sorted(sales_index_new)
with open('D:\YandexDisk\Документы\Обучение\DataAnalisys\Яндекс практикум\YaMyPract\de-project-bibip\de-project-bibip\src\sales_index.txt', 'w+') as si:
    for line in sales_index_sorted:
        si.write(f'{line}\n')

# получение номера строки с нужным vin из car_index
with open('D:\YandexDisk\Документы\Обучение\DataAnalisys\Яндекс практикум\YaMyPract\de-project-bibip\de-project-bibip\src\cars_index.txt', 'r+') as ci:
    cars_index_lines = ci.readlines()
    for line in cars_index_lines:
        current_index_line = line.strip().split(',')
        vin = current_index_line[0]
        current_cars_line = current_index_line[1]
        if vin == "aaa111":
            cars_line = int(current_cars_line)
            

# получение строки с нужным vin из car
with open('D:\YandexDisk\Документы\Обучение\DataAnalisys\Яндекс практикум\YaMyPract\de-project-bibip\de-project-bibip\src\cars.txt', 'r+') as cars:
    lines = cars.readlines()
    current_car_info_raw = lines[cars_line-1]
    current_car_info = current_car_info_raw.strip().split(',')
# запись статуса в нужный список
    current_car_info[4] = 'sold'
# преобразование списка в строку и запись в файл
    new_car_line = f'{current_car_info[0]},{current_car_info[1]},{current_car_info[2]},{current_car_info[3]},{current_car_info[4]}'.ljust(500)+'\n'
    cars.seek((cars_line-1) * (501))
    cars.write(new_car_line)