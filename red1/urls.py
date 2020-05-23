from django.conf.urls import url
from red1.views import user_list, log_in, log_out, sign_up, user_post, DiscoverView, FollowView, UnfollowView


urlpatterns = [
    url(r'^login/$', log_in, name='login'),
    url(r'^logout/$', log_out, name='logout'),
    url(r'^signup/$', sign_up, name='signup'),
    url(r'^$', user_list, name='user_list'),
    url(r'^post$', user_post, name='post'),
    #url(r'^discover/(?P<pk>\d+)/$', DiscoverView.as_view(), name='discover'),
    url(r'^w/(?P<slug>\w+)/$', DiscoverView.as_view(), name='w'),
    url(r'^follow/$', FollowView.as_view(), name='follow'),
    url(r'^unfollow/(?P<target_id>\d+)/$', UnfollowView.as_view(),name='unfollow'),
]