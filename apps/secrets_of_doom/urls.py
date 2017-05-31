from django.conf.urls import url, include
from . import views

# GET "/dashboard" -> dashboard
# GET "/secrets" -> popular_secrets
# POST "/secrets/create" -> create_secret
# GET "/secrets/id/like" -> like
# GET "/secrets/id/delete" -> delete

urlpatterns = [
	url(r'^dashboard$', views.dashboard, name='dashboard'),
	url(r'^secrets$', views.popular_secrets, name='popular_secrets'),
	url(r'^secrets/create$', views.create_secret, name='create_secret'),
	url(r'^secrets/(?P<id>\d+)/like$', views.like, name='like'),
	url(r'^secrets/(?P<id>\d+)/delete$', views.delete, name='delete'),
]

