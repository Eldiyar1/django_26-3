from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from custom_users.forms import CustomRegistrationForm


class Registration(CreateView):
    template_name = "register.html"
    form_class = CustomRegistrationForm
    # form_class = UserCreationForm
    success_url = '/users/'


class AuthLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("users:user_list")

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.all()
