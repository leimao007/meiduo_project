from django.urls import path
from apps.users.views import UsernameCountView

urlpatterns = [
    # check username is duplicated or not
    path('usernames/<username:username>/count/', UsernameCountView.as_view()),
]