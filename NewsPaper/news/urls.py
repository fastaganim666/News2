from django.urls import path
from .views import PostsList, PostDetail, PostsListSearch


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', PostsListSearch.as_view()),
]