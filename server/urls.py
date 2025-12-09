from django.contrib import admin
from django.urls import path, include
from online_menu.views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register_name'),
    path('login/', login_view, name='login'),
    path("order/", order_page, name="order_name"),
    path("api/", include("online_menu.urls")),
    path('dish/<int:dish_id>/', detail_dish, name='detail_dish'),
    path('add_dish/', add_dish, name='add_dish'),
    path('dishes/', dish_list, name='dish_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
