from django.urls import path
from .views import(post_list,
                    ArticleUpdateView,
                    ArticleDeleteView,
                    ArticleCreateView,
                    ArticleDetailView,
                    post_share,
                    CommentCreateView,
                    # post_search
                    )


urlpatterns = [
    path('<int:pk>/edit/',
    ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/',
    ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/',
    ArticleDeleteView.as_view(), name='article_delete'),
    path('', post_list, name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:article_id>/share/', post_share, name='share'),
    # path('search/', post_search, name='search')
    path('new_comment/<int:pk>', CommentCreateView.as_view(), name='new_comment'),
]