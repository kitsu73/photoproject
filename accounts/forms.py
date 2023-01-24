from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
     #連携するモデルを設定
     model = CustomUser
     #フォームで使用するモデルを設定
     fields = ('username', 'email', 'password1', 'password2')