from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("my_orders", views.register_view, name="my_orders"),
    path("menu", views.menu, name="menu"),
    path("add/<str:categ>/<str:name>/<str:price>/<str:size>/<str:cart>/<str:actPrice>", views.add, name="add"),
    path("create_order", views.create_order_view, name="create_order"),
    path("orders", views.orders_view, name="orders"),
    #path("add", views.add, name="add")
    #path("menu/<str:category>", views.menu, name="menu"),

]
