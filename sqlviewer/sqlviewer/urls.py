from django.contrib import admin
from django.urls import path
from viewer.views import SqlDataListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SqlDataListView.as_view(), name='sql-data-list'),
]
