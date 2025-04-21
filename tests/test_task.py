import pytest

from src.task import Category, Product


@pytest.fixture
def setup_data():
    category1 = Category("Одежда", "Различные виды одежды")
    category2 = Category("Электроника", "Электронная техника")
    return category1, category2


def test_category_initialization(setup_data):
    """Проверяем создание категорий"""
    cat1, _ = setup_data
    assert isinstance(cat1, Category)
    assert cat1.name == "Одежда"
    assert cat1.description == "Различные виды одежды"


def test_product_initialization():
    """Проверяем создание продуктов"""
    product = Product("Футболка", "Белая футболка размера M", 500.0, 10)
    assert isinstance(product, Product)
    assert product.name == "Футболка"
    assert product.description == "Белая футболка размера M"
    assert product.price == 500.0
    assert product.quantity == 10


def test_total_categories_count(setup_data):
    """Проверяем подсчёт количества категорий"""
    _, _ = setup_data
    assert Category.count_categories == 2


def test_total_products_count():
    """Проверяем подсчёт количества продуктов"""
    # Создадим две категории с разными наборами продуктов
    product1 = Product("Телефон", "Смартфон последнего поколения", 79999.0, 5)
    product2 = Product("Ноутбук", "Ультракомпактный ноутбук", 89999.0, 3)
    category_electronics = Category("Электроника", "", [product1, product2])

    # Проверим общее количество продуктов
    assert Category.total_products_count == 2