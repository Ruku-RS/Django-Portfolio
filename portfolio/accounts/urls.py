from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/",views.user_login, name='login'),
    path("logout/",views.user_logout, name="logout"),

    path('profile/edit/',views.edit_profile, name="edit_profile"),

    path("password-change/", auth_views.PasswordChangeView.as_view(
        template_name = 'accounts/password_change.html'
        ),
        name= 'password_change',
    ),
    path("password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name='accounts/password_change_done.html'
        ),
        name='password_change_done',
        ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)