from django.urls import path
# viewsモジュールをインポート
from . import views
#viewsをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'),
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),
    
    path('login/',
         #ログイン用のテンプレートフォームをレンダリング
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'
         ),
    
    #ログアウトを実行
    #「http://<ホスト>/logout/」のアクセスに対してdjango.cotrib.auth.views.logoutviewをインスタンス化してログアウトさせる
    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'
         ),
    ]