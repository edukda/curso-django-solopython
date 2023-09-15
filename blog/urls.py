from django.urls import path
from .views import BlogView, BlogViewCreate, BlogViewList

urlpatterns = [
    path('', BlogView.as_view()),
    path('create/', BlogViewCreate.as_view(), name='create'),
    path('list/', BlogViewList.as_view(), name='list')
]