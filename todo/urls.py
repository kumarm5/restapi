from django.conf.urls import url
from todo.views import home, index

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^index/', index)
]
