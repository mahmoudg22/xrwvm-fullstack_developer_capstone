# Uncomment the imports before you add the code
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from djangoapp import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path('register/', views.registration, name='register'),
    # path for login
    path(route='login', view=views.login_user, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
