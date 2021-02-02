
from django.conf.urls import url
from django.views.generic import RedirectView


from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='Home'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$',views.PlayerView.as_view(), name='player'),
    url(r'album/add/$', views.AlbumCreate.as_view(),name='album-add'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(),name='album-update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(),name='album-delete'),
    url(r'album/(?P<pk>[0-9]+)/song/$',views.SongAdd.as_view(),name='song-add'),
    url(r'^song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),
url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
