from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    # /books/
    path('', views.index, name='Index'),
    # /books/5/
    path('<int:book_id>/', views.detail, name='detail'),
    # /books/5/table_content/
    path('<int:book_id>/table_content/',
         views.table_content, name='table_content'),
    # /books/5/read/
    path('<int:book_id>/read/', views.read, name='read'),
]
