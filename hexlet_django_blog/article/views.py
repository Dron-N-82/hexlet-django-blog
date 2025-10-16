from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

# def index(request):
#     return HttpResponse("article")

# class IndexView(View):
#     def get(self, request):
#         context = {"app": "article"}
#         return render(request, "articles/index.html", context)

class IndexView(View):
    def get(self, request, tags, article_id):
        context = {"tags": tags, "article_id": article_id}
        return render(request, "articles/index.html", context)


# def index(request, tags, article_id):
#     return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


def home(request):
    url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(url)

# class IndexView(View):
#     def get(self, request):
# #         if tags is None or article_id is None:
#             url = reverse_lazy('article', args=[tags, article_id])
#             return redirect(url)
#             # return HttpResponse("article")
#         return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
    # def get(self, request):
        # return HttpResponse("article")
    
