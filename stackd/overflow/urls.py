from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'post/', views.post, name='post'),
    url(r'login/', views.user_login, name='user_login'),
    url(r'register/', views.register, name='register'),
    url(r'logout/', views.user_logout, name='user_logout'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<comment_id>[0-9]+)/tu$', views.thumbup_comment, name='tuc')
]
