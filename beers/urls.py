from django.conf.urls import url
from beers.views import first_view

urlpatterns = [
    url(r'^$', first_view, name='first_view'),
]
