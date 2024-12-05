from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Cart, CartProducts, Order, DeliveryMethod
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def category_list(request):
    categories = Category.objects.all()
    user = request.user
    return render(request, 'category_list.html', {'categories': categories, 'user': user})


def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_product, is_created = CartProducts.objects.get_or_create(cart=cart, product=product)

        if not is_created:
            cart_product.quantity += 1
            cart_product.save()

        messages.success(request, 'Ваш товар успешно добавлен в корзину.')

    return render(request, 'product_list.html', {
        'category': category,
        'page_obj': page_obj,
        'messages': messages.get_messages(request)
    })


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/shop')
    else:
        form = UserCreationForm()

    return render(request, 'registration_page.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/shop')
        else:
            return render(request, 'login_page.html', {'error': 'Неверный логин или пароль.'})

    return render(request, 'login_page.html')


def logout_view(request):
    auth_logout(request)
    return redirect('/shop')


def cart_view(request):
    if not request.user.is_authenticated:
        return render(request, 'cart.html', {
            'unauthenticated': True,
            'total_price': 0})

    cart, is_created = Cart.objects.get_or_create(user=request.user)
    cart_products = CartProducts.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_products)

    if request.method == 'POST':
        if 'clear_cart' in request.POST:
            cart.cart_products.all().delete()
            return redirect('/cart')

        elif 'remove_product' in request.POST:
            product_id = request.POST.get('product_id')
            CartProducts.objects.filter(cart=cart, product_id=product_id).delete()
            return redirect('/cart')

    return render(request, 'cart.html', {
        'products': cart_products,
        'total_price': total_price,
        'unauthenticated': False
    })


def checkout(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        phone_number = request.POST.get('phone_number')
        delivery_method_id = request.POST.get('delivery_method')
        delivery_address = request.POST.get('delivery_address')

        cart = Cart.objects.get(user=request.user)

        if not cart.cart_products.exists():
            messages.error(request, 'Корзина пуста, добавьте товары в корзину перед оформлением заказа!')
            return redirect('/checkout')

        total_price = sum(item.product.price * item.quantity for item in cart.cart_products.all())
        product_names = ", ".join([item.product.name for item in cart.cart_products.all()])

        Order.objects.create(
            user=request.user,
            cart=cart,
            delivery_method_id=delivery_method_id,
            delivery_address=delivery_address,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
            total_price=total_price,
            product_name=product_names,
        )

        messages.success(request, 'Заказ успешно оформлен!')
        cart.cart_products.all().delete()

        return redirect('/checkout')

    delivery_methods = DeliveryMethod.objects.all()
    return render(request, 'checkout.html', {'delivery_methods': delivery_methods})
