from django.urls import path
from phones.views import PhoneListView, PhoneDetailView, DeletePhoneView, CreatePhoneView, UpdatePhoneView, Search

urlpatterns = [
    path('phones/', PhoneListView.as_view(), name='phones'),
    path('phones/<int:id>/', PhoneDetailView.as_view()),
    path('phone/<int:id>/delete/', DeletePhoneView.as_view()),
    path('phone/<int:id>/update/', UpdatePhoneView.as_view()),
    path('create_phone/', CreatePhoneView.as_view()),
    path('search/', Search.as_view(), name='search')
]