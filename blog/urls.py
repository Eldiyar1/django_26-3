from django.urls import path
from .views import hello_world_view, posts_view, posts_detail_view, post_create_view, post_update_view, post_delete_view

urlpatterns = [
    path("", hello_world_view),
    path("posts/", posts_view),
    path("post/<int:id>/", posts_detail_view),
    path('post_create/', post_create_view),
    path('post/<int:id>/update/', post_update_view, name='update_post'),
    path('post/<int:id>/delete/', post_delete_view)
]
