from django.urls import path
from .views import *
urlpatterns = [
    path('posts/',PostView.as_view()),
    path('post/<int:post_id>/comments',commentView.as_view()),
    path('post/<int:post_id>',postUpdateDeleteView.as_view()),
    path('comment/<int:pk>',commentUpdateDeleteView.as_view()),
    path('post/<int:pk>/like',LikesUpdateView.as_view()),
]
