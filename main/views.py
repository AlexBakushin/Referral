from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import UserRegisterForm, UserProfileForm
from .models import User


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'main/index.html', context)


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
