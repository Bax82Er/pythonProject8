class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name              # Название продукта
        self.description = description  # Описание продукта
        self.price = price            # Цена продукта (например, 10.99)
        self.quantity = quantity      # Количество продукта в наличии (штуки)


class Category:
    count_categories = 0  # Общее количество созданных категорий
    total_products_count = 0  # Суммарное количество продуктов во всех категориях

    def __init__(self, name: str, description: str, products=None):
        if products is None:
            products = []

        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.products = products  # Список объектов класса Product

        # Увеличиваем общее количество категорий при создании новой категории
        Category.count_categories += 1

        # Подсчитываем количество продуктов и увеличиваем общий счётчик
        for product in products:
            Category.total_products_count += 1