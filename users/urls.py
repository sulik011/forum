from django.urls import path
from .views import SignUpView, post_list

app_name = 'account'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/', post_list, name='user'),
]