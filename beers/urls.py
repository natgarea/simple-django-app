from django.conf.urls import url

from beers.views import first_view, beer_list_view, beer_detail_view

urlpatterns = [
    url(r'^$', first_view, name='first-view'),
    url(r'^beer/list/$', beer_list_view, name='beer-list-view'),
    url(r'^beer/detail/(?P<pk>\d+)/$', beer_detail_view, name='beer-detail-view'),
]