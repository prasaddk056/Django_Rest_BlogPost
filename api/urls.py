from django.urls import path
from . import views

urlpatterns = [
    path("" , views.BlogPostList.as_view() , name = "api-view"),
    path("blogposts/" , views.BlogPostListCreate.as_view() , name = "blogpost-view-create"),
    path("blogposts/<int:pk>/" , views.BlogPostRetrieveUpdateDestroy.as_view() , name="update"),
]
