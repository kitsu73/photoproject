from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    # forms.pyで定義したクラス
    form_class = CustomUserCreationForm
    # レンダリングするテンプレート
    template_name = "signup.html"
    # サインアップ完了後の血ダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self, form):
        # formオブジェクトのフィールド値をデータベースに保存
        user = form.save()
        self.object = user
        #戻り値はスーパークラスのform_validの戻り値
        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"
        