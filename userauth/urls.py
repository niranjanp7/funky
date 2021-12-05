from . import views
from django.urls import path


urlpatterns = [
    path("", views.signup, name="signup"),
    path("userlogin", views.userlogin, name="userlogin"),
    path("userlogout", views.userlogout, name="userlogout"),
    path("userprofile", views.userprofile, name="userprofile"),
    path("levelCleared", views.levelCleared, name="levelCleared"),
]
