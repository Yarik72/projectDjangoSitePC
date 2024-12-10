from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Category(models.Model):
    """
    Модель категории товаров.

    Атрибуты:
        name (str): Название категории.
        image (ImageField): Изображение категории.
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель товара.

    Атрибуты:
        name (str): Название товара.
        price (DecimalField): Цена товара.
        description (TextField): Описание товара.
        image (ImageField): Изображение товара.
        category (ForeignKey): Связь с моделью Category многие к одному.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class DeliveryMethod(models.Model):
    """
    Модель способа доставки.

    Атрибуты:
        name (str): Название способа доставки.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    """
    Модель корзины покупок.

    Атрибуты:
        user (OneToOneField): Связь с моделью User один к одному.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Корзина для пользователя: {self.user.username}"


class CartProducts(models.Model):
    """
    Модель товаров в корзине.

    Атрибуты:
        cart (ForeignKey): Связь с моделью Cart многие к одному.
        product (ForeignKey): Связь с моделью Product многие к одному.
        quantity (PositiveIntegerField): Количество товара в корзине.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} в корзине {self.cart}'


class Order(models.Model):
    """
    Модель заказа.

    Атрибуты:
        user (ForeignKey): Связь с моделью User многие к одному.
        cart (ForeignKey): Связь с моделью Cart многие к одному.
        delivery_method (ForeignKey): Связь с моделью DeliveryMethod многие к одному.
        delivery_address (str): Адрес доставки.
        first_name (str): Имя получателя.
        last_name (str): Фамилия получателя.
        middle_name (str): Отчество получателя (необязательное).
        phone_number (str): Номер телефона получателя.
        total_price (DecimalField): Общая стоимость заказа.
        product_name (str): Название товаров в заказе.
        created_at (DateTimeField): Дата и время создания заказа.
       """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)

    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    product_name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Заказ № {self.id} для {self.user.username}, Дата создания: {self.created_at.strftime("%d.%m.%Y %H:%M")}'


class OrderAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления заказами в админке Django.

    Атрибуты:
        list_display (list): Поля, отображаемые в списке заказов.
        search_fields (list): Поля, по которым можно осуществлять поиск.
    """
    list_display = ('id', 'user', 'product_name', 'total_price', 'created_at')
    search_fields = ('user__username', 'product_name', 'first_name', 'last_name', 'phone_number')
