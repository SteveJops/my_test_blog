from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic import TemplateView, View, DetailView
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

# class SingleDetail(View):
#     def get(self, request, pk):
#         single = get_object_or_404(News, id=pk)
#         return render(request, 'single/single_detail.html', {"one":single})

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


class  NewsCreate(View):
    def get(self, request):
        form = NewsForm()
        print(form)
        return render(request, 'news/news_create.html', {'form': form})

    def post(self, request):
        bound_form = NewsForm(request.POST)
        if bound_form.is_valid():
            new_news = bound_form.save()
            return redirect(new_news)
        return render(request, 'news/news_create.html',  {'form': bound_form})





