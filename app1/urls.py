from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.test,name='test'),
    path('',views.ReviewCsvForm.as_view(),name='csv_home')
]
