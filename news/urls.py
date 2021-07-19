from django.urls import path
from .views import NewsList, NewsUpdate, SingleDetail, NewsCreate

urlpatterns = [
    path('', NewsList.as_view(), name='home'),
    # path('search/', SearchView.as_view(), name='search'),
    path('create/', NewsCreate.as_view(), name = 'creates'),
    path('<slug:slug>/update/', NewsUpdate.as_view(), name = 'updates'),
    path('<slug:slug>/', SingleDetail.as_view(), name='detail')
]