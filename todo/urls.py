from django.conf.urls import url
from todo.views import PostListAPIView

urlpatterns = [
    url(r'^tasks/$', PostListAPIView.as_view()),
]
