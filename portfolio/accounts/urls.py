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

    #Password Change
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

    # Password Reset
    path(
    "password-reset/",
    auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html"
    ),
    name="password_reset",
    ),
    path(
    "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"
    ),
    name="password_reset_done",
    ),
    path(
    "password-reset/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html"
    ),
    name="password_reset_confirm",
    ),
    path(
    "password-reset/complete/",
    auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"
    ),
    name="password_reset_complete",
    ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)