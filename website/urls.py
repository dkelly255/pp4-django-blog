landing_vifrom . import views
from django.urls import path

urlpatterns = [
    path("", views.landing_page, name="home"),
    path("post-list/", views.PostList.as_view(), name="post_list"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
