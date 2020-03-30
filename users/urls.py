from django.conf.urls import url
from users import views as user_view
from django.contrib.auth import views as auth_views
from .views import register, user_login, Manager_login

app_name = 'users'

urlpatterns = [

    url(r'^loginoperator/$', user_login, name='login_op'),
    url(r'^logoutoperator/$', auth_views.LogoutView.as_view(template_name='users/logout_op.html'), name='logout_op'),
    url(r'^loginmanager/$', Manager_login, name='login_mang'),
    url(r'^logoutmanager/$', auth_views.LogoutView.as_view(template_name='users/logout_manager.html'), name='logout_mang'),
    url(r'^register/$', register, name='register')
]