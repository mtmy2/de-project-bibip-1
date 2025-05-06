from models import Car, CarFullInfo, CarStatus, Model, ModelSaleStats, Sale
from decimal import Decimal


class CarService:
    def __init__(self, root_directory_path: str) -> None:
        self.root_directory_path = root_directory_path
        self.cell_size = 500
        self.models = f'{self.root_directory_path}/models.txt'
        self.models_i = f'{self.root_directory_path}/models_index.txt'
        self.cars = f'{self.root_directory_path}/cars.txt'
        self.cars_i = f'{self.root_directory_path}/cars_index.txt'
        self.sales = f'{self.root_directory_path}/sales.txt'
        self.sales_i = f'{self.root_directory_path}/sales_index.txt'

    # создание файлов если их еще нет
    def init_file(self, file_name):
        with open(f'{self.root_directory_path}/{file_name}', 'w') as f:
            pass
    def init_files(self):
        file_names = ['cars.txt', 'models.txt', 'sales.txt', 'cars_index.txt', 'models_index.txt', 'sales_index.txt']
        for file_name in file_names:
            self.init_file(file_name)

    # Задание 1. Сохранение автомобилей и моделей
    def add_model(self, model: Model) -> Model:
        # запись в файл model.txt
        with open(self.models, 'a') as m:
            m.write(f'{model.id},{model.name},{model.brand}'.ljust(self.cell_size)+'\n')

        # Запись в файл models_index.txt
        with open(self.models, 'r+') as mi:
            lines = mi.readlines()
            line_number = str(len(lines)+1)
            lines.append(f'{model.name},{line_number}'+'\n')
            models_index_sorted = sorted(lines)
            mi.seek(0)
            mi.writelines(models_index_sorted) 

    # Задание 1. Сохранение автомобилей и моделей
    def add_car(self, car: Car) -> Car:
        # запись в файл cars.txt
        with open(self.cars, 'a') as cars:
            cars.write(f'{car.vin},{car.model},{car.price},{car.date_start},{car.status}'.ljust(self.cell_size)+'\n')

        # Запись в файл cars_index.txt
        with open(self.cars_i, 'r+') as ci:
            current_index = list(ci.readlines())
            line_number = len(current_index)+1
            current_index.append(f'{car.vin},{line_number}'+'\n')
            cars_index_sorted = sorted(current_index)
            ci.seek(0)
            ci.writelines(cars_index_sorted) 

    # Задание 2. Сохранение продаж.
    def sell_car(self, sale: Sale) -> Car:
        #cars_line = 0
        # запись в файл sales.txt
        with open(self.sales, 'a') as sales:
            sales.write(f'{sale.sales_number},{sale.car_vin},{sale.sales_date},{sale.cost}'.ljust(self.cell_size)+'\n')

        # Запись в файл sales_index.txt
        with open(self.sales_i, 'r+') as si:
            readlines=si.readlines()
            line_number = len(readlines)
            if line_number == 0:
                readlines = [f'{sale.car_vin},{line_number+1}'+'\n']
            else:
                readlines.append(f'{sale.car_vin},{line_number+1}'+'\n')
            sales_index_sorted = sorted(readlines)
        with open(self.sales_i, 'a') as si:
            for line in sales_index_sorted:
                si.write(f'{line}')

        # получение номера строки с нужным vin из car_index
        with open(self.cars_i, 'r+') as ci:
            cars_index_lines = ci.readlines()
            for line in cars_index_lines:
                current_index_line = line.strip().split(',')
                vin = current_index_line[0]
                current_cars_line = current_index_line[1]
                if vin == sale.car_vin:
                    cars_line = int(current_cars_line)

            

        # получение строки с нужным vin из cars
        with open(self.cars, 'r+') as cars:
            lines = cars.readlines()
            current_car_info_raw = lines[cars_line-1]
            current_car_info = current_car_info_raw.strip().split(',')
        # запись статуса в нужный список
            current_car_info[4] = 'sold'
        # преобразование списка в строку и запись в файл
            new_car_line = f'{current_car_info[0]},{current_car_info[1]},{current_car_info[2]},{current_car_info[3]},{current_car_info[4]}'.ljust(self.cell_size)+'\n'
            cars.seek((cars_line-1) * (self.cell_size+1))
            cars.write(new_car_line)


    # Задание 3. Доступные к продаже
    def get_cars(self, status: CarStatus) -> list[Car]:
        raw_cars = []
        available_cars = []
        with open(self.cars, 'r+') as cars:
            for raw_line in cars:            
                line = raw_line.strip().split(',')
                if line[-1].strip() == 'available':
                    car_data = {
                        "vin": line[0],
                        "model": int(line[1]),
                        "price": line[2],
                        "date_start": line[3].strip(),
                        "status": CarStatus(line[4].strip()),
                        }
                    available_cars.append(Car(**car_data))
        return available_cars
                    
                    
 
    # Задание 4. Детальная информация
    def get_car_info(self, vin: str) -> CarFullInfo | None:
        # получение номера строки с нужным vin из car_index
        with open(self.cars_i, 'r+') as ci:
            cars_index_lines = ci.readlines()
            for line in cars_index_lines:
                current_index_line = line.strip().split(',')
                current_vin = current_index_line[0]
                current_cars_line = current_index_line[1]
                if vin == current_vin:
                    cars_line = int(current_cars_line)
        # получение строки с нужным vin из car
        with open(self.cars, 'r+') as cars:
            lines = cars.readlines()
            current_car_info = lines[cars_line-1].strip().split(',')
            current_model = current_car_info[1]
            current_status = current_car_info[4]
            price = current_car_info[2]
            date_start = current_car_info[3]


        # получение номера строки с нужной моделью из model_index
        with open(self.models_i, 'r+') as mi:
            models_index_lines = mi.readlines()
            for line in models_index_lines:
                current_model_index = line.strip().split(',')
                model = current_model_index[0]
                current_models_line = current_model_index[1]
                if model == current_model:
                    models_line = int(current_models_line)
        # получение строки с нужной моделью из models
        with open(self.models, 'r+') as m:
            lines = m.readlines()
            current_model_info = lines[models_line-1].strip().split(',')
            current_brand = current_model_info[2]


        # получение номера строки с нужным vin из sales_index
        with open(self.sales_i, 'r+') as si:
            vin_index_lines = si.readlines()
            for line in vin_index_lines:
                current_sales_index = line.strip().split(',')
                vin = current_sales_index[0]
                current_vin_line = current_sales_index[1]
                if vin == current_vin_line:
                    sales_line = int(current_vin_line)
        # получение строки с нужным vin из sales
        with open(self.sales, 'r+') as s:
            lines = s.readlines()
            current_sale_info = lines[sales_line-1].strip().split(',')
            if current_status == 'sold':
                current_sales_date = None
                current_sales_cost = None
            else:
                current_sales_date = current_sale_info[2]
                current_sales_cost = current_sale_info[3]

        return CarFullInfo(vin, current_model, current_brand, price, date_start, current_status, current_sales_date, current_sales_cost)
            

   
    # Задание 5. Обновление ключевого поля
    def update_vin(self, vin: str, new_vin: str) -> Car:
        i=-1
        #нахождение строки со старым vin
        with open(self.cars_i, 'r+') as ci:
            lines = ci.readlines()
            for line in lines:
                i=i+1
                line_list = line.strip().split(',')
                if vin == line_list[0]:
                    cars_line_number = int(line_list[1])
                    # обновление vin в car_index
                    lines[i] = new_vin + cars_line_number + '\n'  
                    with open(self.cars_i, 'r+') as ci:
                        ci.seek(0)
                        ci.writelines(lines)
                    break    
        # обновление vin в cars  
        with open(self.cars, 'r+') as cars:
            lines = cars.readlines()
            line_list = lines[cars_line_number-1].strip().split(',')
            line_list[0] = new_vin  
            lines[cars_line_number-1] = ','.join(line_list) + '\n'  
            cars.seek(0)
            cars.writelines(lines)
        
    # Задание 6. Удаление продажи
    def revert_sale(self, sales_number: str) -> Car:
        # поиск строки с нужной продажей
        with open(self.sales_i, 'r') as si:
            lines = si.readlines()
            for line in lines:
                line_list = line.strip().split(',')
                if line_list[0] == sales_number:
                    sales_row_number = int(line_list[1]) - 1
                    break
                else:
                    return None
        
        with open(self.sales, 'r') as s:
            lines = s.readlines()
            line = lines[sales_row_number].strip().split(',')
            vin = line[1].strip()
            if line[0] == sales_number and self.is_deleted == False:
                self.is_deleted = True

        with open(self.cars_i, 'r') as ci:
            lines = ci.readlines()                   
            for line in lines:
                lines_list = line.strip().split(',')
                cars_vin = lines_list[0].strip()           
                if vin == cars_vin:
                    cars_row_number = int(parts[1].strip()) - 1
                    break
          
        with open(self.cars, 'r+') as cars:
            lines = cars.readlines()
            lines_list = lines[cars_row_number].strip().split(',')
            lines_list[-1] = 'available'  
            lines[cars_row_number] = ','.join(lines_list) + '\n'  
            cars.seek(0)
            cars.writelines(lines)
    
    # Задание 7. Самые продаваемые модели
    def top_models_by_sales(self) -> list[ModelSaleStats]:
        sales_dict: dict[int, int] = {}
        cars_dict: dict[str, int] = {}
        prices: dict[int, Decimal] = {}
        result = []

        # формирование словаря vin - model_id
        with open(self.cars, 'r') as cars:
            lines = cars.readlines()
            for line in lines:
                line_list = line.strip().split(',')
                cars_dict[line_list[0]] = int(line_list[1])

        # формирование словаря model_id - количество продаж
        with open(self.sales, 'r') as s:
            lines = s.readlines()
            for line in lines:
                line_list = line.strip().split(',')
                model = cars_dict[vin]
                vin = line_list[1].strip()  
                price = Decimal(line_list[2])
                if vin in cars_dict:
                    sales_dict[model] = sales_dict[model] + 1
                    prices[model] = price

        # сортировка
        sorted_models: list[int] = sorted(
            sales_dict.keys(),
            key=lambda x: (-sales_dict[x], -prices.get(x, Decimal(0)))
        )[:3]

        # подтягивание модели и брнеда по model_id в отсортированныый список
        for item in sorted_models:
            item_list = item.strip().split(',')
            with open(self.models, 'r',) as m:
                lines = m.readlines()
                for line in lines:
                    line_list = line.strip().split(',')
                    if item_list[1] == line_list[0]:
                        result.append(ModelSaleStats(
                            car_model_name=line_list[1],
                            brand=line_list[2],
                            sales_number=item_list[1]
                        ))
        return result

