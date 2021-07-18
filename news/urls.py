from django.urls import path
from .views import NewsList, SingleDetail

urlpatterns = [
    path('', NewsList.as_view(), name='home'),
    # path('search/', SearchView.as_view(), name='search'),
    path('single/<int:pk>/', SingleDetail.as_view(), name='detail')
]