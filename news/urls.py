from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('news-details/<slug>',views.news_details,name= 'news-details'),
    path('slider-details/<slug>',views.slider_details,name= 'slider_details' ),
    path('login',views.user_login,name='login'),
    path('register',views.register,name='register'),
    path('users',views.users,name='users'),
    path('logout',views.user_logout,name='logout'),
    path('password-reset',auth_views.PasswordResetView.as_view(template_name = 'pages/accounts/password-reset.html'),name ='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = 'pages/accounts/password-reset-confirm.html'),name ='password-reset-confirm'),
    path('password_reset_done',auth_views.PasswordChangeDoneView.as_view(template_name = 'pages/accounts/password_reset_done.html'),name ='password_reset_done'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name = 'pages/accounts/password_reset_complete.html'),name ='password_reset_complete')
    
]