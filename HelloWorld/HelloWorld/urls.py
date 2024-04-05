from django.urls import path

from . import view, search,search2
from django.urls import re_path as url

urlpatterns = [
    path('test_run/', view.test_run),
    path('test_run2/', view.test_run2),
    path('test_run3/', view.test_run3),
    path('test_run4/', view.test_run4),
    path('test_run5/', view.test_run5),
    path('test_run6/', view.test_run6),
    url(r'^hello/$', view.test_run),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$',search2.search_post)
]

