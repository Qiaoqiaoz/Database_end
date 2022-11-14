from django.urls import path
from . import views

urlpatterns = [
    # 用户登录
    path('',views.toLogin_view,name = 'toLogin'),
    path('index/',views.Login_view,name = 'Login'),
    path('toRegister/',views.toRegister,name = 'toRegister'),
    path('register/',views.register_view,name = 'register'),
    # path('toDelete/',views.delete_view),
    # path('delete/',views.delete),
    # path('toSearch/',views.toSearch),
    # path('search/',views.search),
    # path('toUpdate/',views.toUpdate),
    # path('update/',views.update),
    # 商家
    # path('toRegister_rest/',views.register_rest_view),
    # path('register_rest/',views.register_rest),
    # path('toDelete_rest/',views.delete_rest_view),
    # path('delete_rest/',views.delete_rest),
    # path('toSearch_rest/',views.search_rest_view),
    # path('search_rest/',views.search_rest),
    # path('toUpdate_rest/',views.update_rest_view),
    # path('update/',views.update_rest),
    # food
    # path('toRegister_food/',views.register_food_view),
    # path('register_food/',views.register_food),
    # path('toDelete_food/',views.delete_food_view),
    # path('delete_food/',views.delete_food),
    # path('toSearch_food/',views.search_food_view),
    # path('search_food/',views.search_food),
    # path('toUpdate_food/',views.update_food_view),
    # path('update_food/',views.update_food),
]