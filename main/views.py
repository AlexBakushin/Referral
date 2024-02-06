from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .forms import UserRegisterForm, UserProfileForm
from .models import User
from django.core.mail import send_mail
from django.conf import settings
import datetime
import random
from django.shortcuts import get_object_or_404


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

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject='Поздравляю с регистрацией',
            message=f'Ваш реферальный код: {self.object.referral_code}\n'
                    f' Его срок годности до {datetime.datetime.now()+datetime.timedelta(days=5)}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        for referral in User.objects.all():
            if referral.owner is not None and self.request.user.referral_code == referral.owner:
                self.request.user.referrals.add(referral)
                self.request.user.save()
        return self.request.user


def view(request, pk):
    referral = User.objects.get(pk=pk)
    context = {
        'title': 'Просмотр',
        'object': referral,
    }
    return render(request, 'main/view.html', context)


def generate_new_code(request):
    new_ref_code = random.randint(1000000, 9999999)
    send_mail(
        subject='Вы сменили реферальный код',
        message=f'Ваш новый реферальный код: {new_ref_code}\n'
                f' Его срок годности до {datetime.datetime.now() + datetime.timedelta(days=5)}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.referral_code(new_ref_code)
    request.user.save()
    return redirect(reverse('profile'))
