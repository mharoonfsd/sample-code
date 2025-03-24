"""client urls for library app."""


from django.conf.urls import url
from .views import (Login, _logout, rack_list,
                    rack_detail, book_detail, SearchList,
                    invalid_login, disabled_login)


urlpatterns = [
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^login/invalid/$', invalid_login, name="login-invalid"),
    url(r'^login/disabled/$', disabled_login, name="login-disabled"),
    url(r'^logout/$', _logout, name="logout"),
    url(r'rack/$', rack_list, name="rack-list"),
    url(r'rack/(?P<primary_key>[0-9]+)/$', rack_detail, name="rack-detail"),
    url(r'book/(?P<primary_key>[0-9]+)/$', book_detail, name="book-detail"),
    url(r'search/$', SearchList.as_view(), name="search"),
]
