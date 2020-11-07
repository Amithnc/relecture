from django .urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('login/',
        LoginView.as_view(
            template_name='admin/login.html',
            extra_context={
                'site_header': 'Log in to RElecture',
                'site_title' : 'Login page-organization',
            })),
    path('',views.homepage,name='homepage')        
]