from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.showindex, name='index'),
    path('',views.save, name='save'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update')
]