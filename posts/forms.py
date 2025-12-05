from django import forms
from django.core.exceptions import ValidationError
from .models import ReallyUser

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True, label="Электронная почта")
    password1 = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', required=True, widget=forms.PasswordInput)
    avatar = forms.ImageField(label='Аватар', required=True)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Пароли не совпадают.', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = ReallyUser
        fields = ('username', 'email', 'password1', 'password2', 'avatar')