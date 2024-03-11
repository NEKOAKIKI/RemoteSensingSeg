from django.urls import path, re_path
from api.views import login, user, file, record

urlpatterns = [
    path('login/', login.LoginView.as_view()),
    path('sign/', login.SignView.as_view()),
    path('userlur/', user.UserLurView.as_view()),
    path('recorddel/', record.RecordDelView.as_view()),
    path('file/', file.FileView.as_view()),
]