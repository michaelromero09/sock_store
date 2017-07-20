from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'manage_users_index'),
    # url(r'^add_user_page$', views.add_user_page, name = 'manage_users_add_user_page'),
    # url(r'^add_user$', views.add_user_to_db, name = 'manage_users_add_user'),
    url(r'^edit_user_page/(?P<id>\d+)$', views.edit_user_page, name = 'manage_users_edit_user_page'),
    url(r'^edit_user$', views.edit_user, name = 'manage_users_edit_user'),
    url(r'^delete_user$', views.delete_user_from_db, name = 'manage_users_delete_user'),
]