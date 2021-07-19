from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic import TemplateView, View, DetailView
from django.utils import timezone
from .models import News
from django.db.models import Q
from .forms import NewsForm

# Create your views here.

class NewsList(ListView):
    """ List of articles"""
    model = News
    # queryset = News.objects.all()
    context_object_name = 'news'

    def get_queryset(self):
        search_query = self.request.GET.get('q', '')
        if search_query:
            post = News.objects.filter(Q(title__icontains=search_query)| Q(text_min__icontains=search_query))
        else:
           post = News.objects.all()

        return post

class AboutTemplate(TemplateView):
    template_name = 'aboutme.html'

class SingleDetail(DetailView):
    model = News
    context_object_name = 'one'
    slug_field = "slug"
    template_name = "single/single_detail.html"



# class SearchView(ListView):
#     """Search Articles"""
#     paginate_by = 2
#     template_name = 'news_list.html'

#     def get_queryset(self):
# Q(title__icontains=search_query)| Q(text_min__icontains=search_query)
#         query = self.request.GET.get("q").capitalize()
#         print(self.request.GET)
#         context = News.objects.filter(title__icontains=query) 
#         print(context)
#         return context

# toDO delete method to user
class  NewsCreate(View):
    def get(self, request):
        form = NewsForm()
        return render(request, 'news/news_create.html', {'form': form})

    def post(self, request):
        bound_form = NewsForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_news = bound_form.save(commit=False)
            new_news.user = request.user
            new_news.created = timezone.now()
            new_news.save()
            return redirect(new_news)
        return render(request, 'news/news_create.html',  {'form': bound_form})


class NewsUpdate(View):
    def get(self, request, slug):
        news_update = News.objects.get(slug__iexact=slug)
        bound_form = NewsForm(instance=news_update)
        return render(request, 'news/news_update.html', {'form': bound_form, 'news': news_update})

    def post(self, request, slug):
        news_update = News.objects.get(slug__iexact=slug)
        bound_form = NewsForm(request.POST, request.FILES, instance=news_update)

        if bound_form.is_valid():
            new_news_update = bound_form.save()
            return redirect(new_news_update)
        return render(request, 'news/news_update.html', {'form': bound_form, 'news': news_update})





