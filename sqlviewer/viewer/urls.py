from django.urls import path
from .views import SqlDataListView

urlpatterns = [
    path('', SqlDataListView.as_view(), name='sql-data-list'),
]
