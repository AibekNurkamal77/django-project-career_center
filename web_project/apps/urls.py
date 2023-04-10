from .views import *
from django.urls import path
urlpatterns = [
    path('', Index, name='vakansi'),
    path('auth/create_account/', AuthCreate, name='auth_create_account_url'),
    path('teacher_post/create/', TeacherCreate.as_view(), name='teacher_create_url'),
    path('auth/create_account/registration/', Registration, name='registration_url')

]
