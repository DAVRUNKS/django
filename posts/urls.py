from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='post_home'),
    path("greet/", views.greet, name="greet_home"),
    path("posts/", views.return_all_posts, name="all-posts"),
    path("post/<int:post_id>/", views.return_one_post, name="get_one_post"),
    path("about/", views.AboutPageView.as_view, name="post_about"),
    path("services/", views.services, name="post_services"),
    path('create_post', views.CreatePostView.as_view(), name="create_post"),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),  # Corrected line
    path('post/<int:post_id>', views.update_post, name='update_post'),
]
