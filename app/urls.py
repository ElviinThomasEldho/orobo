from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('transactions/', views.transactions, name="transactions"),
    path('quotation/', views.quotation, name="quotation"),
    path('inventory/', views.inventory, name="inventory"),
    path('material/', views.material, name="material"),
    path('delivery/', views.delivery, name="delivery"),
]