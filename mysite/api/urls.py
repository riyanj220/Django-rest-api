from django.urls import path
from . import views

urlpatterns  = [
    path ("blogposts/" , views.BlogPostListCreate.as_view() , 
          name = 'blogpost-view-create'),
    path ("blogposts/<int:pk>/" , views.BlogPostRetriveUpdateDestroy.as_view() , 
          name = "update")
]