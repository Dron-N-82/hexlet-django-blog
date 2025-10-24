from django.urls import path
from hexlet_django_blog.article.views import *
# from hexlet_django_blog.article import views


urlpatterns = [
    # path("", views.index, name='index'),
    # path("", views.home, name='home'),
    path('', IndexView.as_view(), name='index'),
    # path('<str:tags>/<int:article_id>/', IndexView.as_view(), name='article'),
    # path('<str:tags>/<int:article_id>/', views.index, name='article'),
    path("<int:id>/", ArticleView.as_view(), name='article'),
    path("create/", CreateArticleView.as_view(), name='article_add'),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="articles_update"),
    path("<int:id>/delete/", ArticleFormDeleteView.as_view(), name="articles_delete"),
]