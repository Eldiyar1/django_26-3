from django.urls import path
from .views import Registration, AuthLoginView, UserListView

app_name = 'users'
urlpatterns = [
    path('register/', Registration.as_view(), name='registration'),
    path('login/', AuthLoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user_list')
]