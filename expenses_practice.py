# Список покупок
purchases = [
    {"item": "Книга по Python", "category": "Образование", "price": 1500},
    {"item": "Кофе", "category": "Еда", "price": 250},
    {"item": "Подписка на музыку", "category": "Развлечения", "price": 0},  # Бесплатный период
    {"item": "Курс по Git", "category": "Образование", "price": 3000},
]


def show_purchase_details(item, category, price):
    print(f"Товар: {item}, Категория: {category}, Стоимость: {price} руб")


paid_purchaces = [product for product in purchases if product["price"] > 0]
show_purchase_details(**paid_purchaces[0])  # Товар: Книга по Python, Категория: Образование, Стоимость: 1500 руб
