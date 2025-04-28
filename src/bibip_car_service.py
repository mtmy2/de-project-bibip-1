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
                cars_index_new = ci.readlines().append(f'{model.name},{line_number}'+'\n')
            cars_index_sorted = sorted(cars_index_new)
            for line in cars_index_sorted:
                ci.write(f'{line}\n')

    # Задание 2. Сохранение продаж.
    def sell_car(self, sale: Sale) -> Car:
        raise NotImplementedError

    # Задание 3. Доступные к продаже
    def get_cars(self, status: CarStatus) -> list[Car]:
        raise NotImplementedError

    # Задание 4. Детальная информация
    def get_car_info(self, vin: str) -> CarFullInfo | None:
        raise NotImplementedError

    # Задание 5. Обновление ключевого поля
    def update_vin(self, vin: str, new_vin: str) -> Car:
        raise NotImplementedError

    # Задание 6. Удаление продажи
    def revert_sale(self, sales_number: str) -> Car:
        raise NotImplementedError

    # Задание 7. Самые продаваемые модели
    def top_models_by_sales(self) -> list[ModelSaleStats]:
        raise NotImplementedError
