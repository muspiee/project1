from django.urls import path
from .views import home, allProfile, delete

urlpatterns = [
    path('', home, name='home'),
    path('allProfile/', allProfile, name='allProfile'),
    path('delete/<int:id>/', delete, name='delete')
]
