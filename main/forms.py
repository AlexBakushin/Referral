from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'owner', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     for code in User.objects.all().referral_code:
    #         print(code)
    #         if self.cleaned_data.get("owner") == code:
    #
    #         return user


class UserProfileForm(UserChangeForm):

    # def get_form(self, form_class=None):
    #     """
    #     эта функция фильтрует выборку рефералов, на те, чей хозяин - текущий пользователь
    #     """
    #     form = super(UserProfileForm, self).get_form(form_class)
    #     # form.fields['referrals'].queryset = User.objects.filter(owner=self.request.user.username)
    #
    #     return form
    # def clean_other_field(self):
    #     for user_code in User.objects.all().owner:
    #         if self.cleaned_data.get("owner") == user_code:
    #
    #
    #         return data

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
