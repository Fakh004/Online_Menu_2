from django.contrib import admin
from django.urls import path, include
from online_menu.views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("order/", order_page, name="order_name"),
    path("api/", include("online_menu.urls")),
    path('dish/<int:dish_id>/', detail_dish, name='detail_dish'),
    path('add_dish/', add_dish, name='add_dish'),
    path('dishes/', dish_list, name='dish_list'),
    path('dish/edit/<int:dish_id>/', dish_edit, name='dish_edit'),
    path('dish/delete/<int:dish_id>/', dish_delete, name='dish_delete'),
    path('order/', order_view, name='order_view'),
    path('order/success/', order_success, name='order_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
