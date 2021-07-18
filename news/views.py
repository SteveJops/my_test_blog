from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic import TemplateView, View, DetailView
from .models import News

# Create your views here.

class NewsList(ListView):
    """ List of articles"""
    model = News
    queryset = News.objects.all()
    context_object_name = 'news'



class AboutTemplate(TemplateView):
    template_name = 'aboutme.html'

# class SingleDetail(View):
#     def get(self, request, pk):
#         single = get_object_or_404(News, id=pk)
#         return render(request, 'single/single_detail.html', {"one":single})

class SingleDetail(DetailView):
    model = News
    context_object_name = 'one'
    slug_field = "id"
    template_name = "single/single_detail.html"

class SearchView(ListView):
    """Search Articles"""
    # paginate_by = 1
    template_name = 'news_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q").capitalize()
        context = News.objects.filter(title__icontains=query) 
        print(context)
        return context





