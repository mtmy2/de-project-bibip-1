from models import Car, CarFullInfo, CarStatus, Model, ModelSaleStats, Sale


class CarService:
    def __init__(self, root_directory_path: str) -> None:
        self.root_directory_path = root_directory_path

    # Задание 1. Сохранение автомобилей и моделей
    def add_model(self, model: Model) -> Model:
        # запись в файл model.txt
        with open(f'{self.root_directory_path}/models.txt', 'a') as m:
            m.write(f'{model.id},{model.name},{model.brand}'.ljust(500)+'\n')

        # Запись в файл models_index.txt
        with open(f'{self.root_directory_path}/models_index.txt', 'w+') as mi:
            line_number = str(len(mi.readlines())+1)
            if mi.readlines() == []:
                model_index_new = [f'{model.name},{line_number}'+'\n']
            else:
                model_index_new = mi.readlines().append(f'{model.name},{line_number}'+'\n')
            models_index_sorted = sorted(model_index_new)
            for line in models_index_sorted:
                mi.write(f'{line}\n')


        


    # Задание 1. Сохранение автомобилей и моделей
    def add_car(self, car: Car) -> Car:
        # запись в файл cars.txt
        with open(f'{self.root_directory_path}/cars.txt', 'a') as cars:
            cars.write(f'{car.vin},{car.model},{car.price},{car.date_start},{car.status}'.ljust(500)+'\n')

        # Запись в файл cars_index.txt
        with open(f'{self.root_directory_path}/cars_index.txt', 'w+') as ci:
            line_number = len(ci.readlines())+1
            if ci.readlines() == []:
                cars_index_new = [f'{car.vin},{line_number}'+'\n']
            else:
                cars_index_new = ci.readlines().append(f'{car.vin},{line_number}'+'\n')
            cars_index_sorted = sorted(cars_index_new)
            for line in cars_index_sorted:
                ci.write(f'{line}\n')

    # Задание 2. Сохранение продаж.
    def sell_car(self, sale: Sale) -> Car:
        # запись в файл sales.txt
        with open(f'{self.root_directory_path}/sales.txt', 'w+') as sales:
            sales.write(f'{sale.sales_number},{sale.car_vin},{sale.sales_date},{sale.cost}'.ljust(500)+'\n')

        # Запись в файл sales_index.txt
        with open(f'{self.root_directory_path}/sales_index.txt', 'w+') as si:
            line_number = len(si.readlines())+1
            if si.readlines() == []:
                sales_index_new = [f'{sale.sales_number},{line_number}'+'\n']
            else:
                sales_index_new = si.readlines().append(f'{sale.car_vin},{line_number}'+'\n')
            sales_index_sorted = sorted(sales_index_new)
            for line in sales_index_sorted:
                si.write(f'{line}\n')

        # получение номера строки с нужным vin из car_index
        with open(f'{self.root_directory_path}/car_index.txt', 'w+') as ci:
            cars_index_lines = ci.readlines()
            for line in cars_index_lines:
                current_index_line = line.strip().split(',')
                vin = current_index_line[0]
                current_cars_line = current_index_line[1]
                if vin == sale.car_vin:
                    cars_line = int(current_cars_line)

        # получение строки с нужным vin из car
        with open(f'{self.root_directory_path}/cars.txt', 'w+') as cars:
            lines = cars.readlines()
            current_car_info = lines[cars_line].strip().split(',')
        # запись статуса в нужный список
            current_car_info[4] = 'sold'
        # преобразование списка в строку и запись в файл
            new_car_line = f'{urrent_car_info[0]},{urrent_car_info[1]},{urrent_car_info[2]},{urrent_car_info[3]},{urrent_car_info[4]}'.ljust(500)+'\n'
            cars.seek((cars_line-1) * (501))
            cars.write(new_car_line)


    # Задание 3. Доступные к продаже
    def get_cars(self, status: CarStatus) -> list[Car]:
        raise NotImplementedError

    # Задание 4. Детальная информация
    def get_car_info(self, vin: str) -> CarFullInfo | None:
        # получение номера строки с нужным vin из car_index
        with open(f'{self.root_directory_path}/car_index.txt', 'w+') as ci:
            cars_index_lines = ci.readlines()
            for line in cars_index_lines:
                current_index_line = line.strip().split(',')
                current_vin = current_index_line[0]
                current_cars_line = current_index_line[1]
                if vin == current_vin:
                    cars_line = int(current_cars_line)
        # получение строки с нужным vin из car
        with open(f'{self.root_directory_path}/cars.txt', 'w+') as cars:
            lines = cars.readlines()
            current_car_info = lines[cars_line].strip().split(',')
            current_model = current_car_info[1]
            current_status = current_car_info[4]
            price = current_car_info[2]
            date_start = current_car_info[3]


        # получение номера строки с нужной моделью из model_index
        with open(f'{self.root_directory_path}/models_index.txt', 'w+') as mi:
            models_index_lines = mi.readlines()
            for line in models_index_lines:
                current_model_index = line.strip().split(',')
                model = current_model_index[0]
                current_models_line = current_model_index[1]
                if model == current_model:
                    models_line = int(current_models_line)
        # получение строки с нужной моделью из models
        with open(f'{self.root_directory_path}/models.txt', 'w+') as m:
            lines = m.readlines()
            current_model_info = lines[models_line].strip().split(',')
            current_brand = current_model_info[2]


        # получение номера строки с нужным vin из sales_index
        with open(f'{self.root_directory_path}/sales_index.txt', 'w+') as si:
            vin_index_lines = si.readlines()
            for line in vin_index_lines:
                current_sales_index = line.strip().split(',')
                vin = current_sales_index[0]
                current_vin_line = current_sales_index[1]
                if vin == current_vin_line:
                    sales_line = int(current_vin_line)
        # получение строки с нужным vin из sales
        with open(f'{self.root_directory_path}/sales.txt', 'w+') as s:
            lines = s.readlines()
            current_sale_info = lines[sales_line].strip().split(',')
            if current_status == 'sold':
                current_sales_date = None
                current_sales_cost = None
            else:
                current_sales_date = current_sale_info[2]
                current_sales_cost = current_sale_info[3]

        return CarFullInfo(vin, current_model, current_brand, price, date_start, current_status, current_sales_date, current_sales_cost)
            

        
            


    # Задание 5. Обновление ключевого поля
    def update_vin(self, vin: str, new_vin: str) -> Car:
        raise NotImplementedError

    # Задание 6. Удаление продажи
    def revert_sale(self, sales_number: str) -> Car:
        raise NotImplementedError

    # Задание 7. Самые продаваемые модели
    def top_models_by_sales(self) -> list[ModelSaleStats]:
        raise NotImplementedError
