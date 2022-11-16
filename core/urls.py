from django.urls import path
from core.views import *

urlpatterns = [
    path('user/', user_api_view, name="user_api"),
    path('autor/<int:pk>/', autor_api_view, name="autor_api"),
    path('book/<int:pk>/', book_api_view, name="book_api"),
    path('book/', books_api_view, name="book_api"),
    path('loan/', loan_api_view, name="loan_api"),
    path('loan/<int:pk>/', loan_detail_api_view, name= "loan_detail_api"),
]