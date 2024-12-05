"""
URL configuration for online_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import category_list, product_list, register_view, login_view, logout_view,cart_view, checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', category_list),
    path('category/<int:category_id>/', product_list,name='product_list'),
    path('cart/', cart_view),
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('checkout/', checkout),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
