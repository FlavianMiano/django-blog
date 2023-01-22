from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailview, AppPostView, UpdatePostView, DeletePostView, AppCategoryView, CategoryView, CategoryListView

urlpatterns = [
    #path('', views.home, name = 'home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailview.as_view(), name='article-detail'),
    path('add_post/', AppPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/del', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AppCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category_list'),
    #path('like/<int:ok>', LikeView, name='like_post'),
]
