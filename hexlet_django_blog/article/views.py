from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
# from django.http import HttpResponse
from django.views import View
# from django.shortcuts import redirect
from django.urls import reverse
from .forms import ArticleForm
#from .models import ArticleComment
from hexlet_django_blog.article.models import Article
from django.contrib import messages

# def index(request):
#     return HttpResponse("article")

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        context = {"articles": articles}
        return render(request, "articles/index.html", context)

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )
# class IndexView(View):
#     def get(self, request):
#         context = {"app": "article"}
#         return render(request, "articles/index.html", context)

# class IndexView(View):
#     def get(self, request, tags, article_id):
#         context = {"tags": tags, "article_id": article_id}
#         return render(request, "articles/index.html", context)


# def index(request, tags, article_id):
#     return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


# def home(request):
#     url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
#     return redirect(url)

# class IndexView(View):
#     def get(self, request):
# #         if tags is None or article_id is None:
#             url = reverse_lazy('article', args=[tags, article_id])
#             return redirect(url)
#             # return HttpResponse("article")
#         return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
    # def get(self, request):
        # return HttpResponse("article")
    
class CreateArticleView(View):
    # если метод POST, то мы обрабатываем данные
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данные формы на корректность
            form.save()
            return redirect(reverse('index'))
        else:
            return render(request, "articles/create.html", {"form": form})
        

    # если метод GET, то создаем пустую форму
    def get(self, request, *args, **kwargs):
        form = ArticleForm()  # Создаем экземпляр нашей формы
        return render(
            request, "articles/create.html", {"form": form}
        )  # Передаем нашу форму в контексте


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Статья обновлена.")
            return redirect(reverse("index"))
        
        messages.error(request, 'Произошла ошибка при сохранении.')
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )

class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect(reverse('index'))