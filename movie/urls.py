
from django.urls import path
from .views import HomeView, MovieList , MovieDetail , MovieCategory , MovieLanguage , MovieSearch , MovieYear


app_name='movie'

urlpatterns = [
    path('', HomeView.as_view() , name='homepage'),
    path('movie_list', MovieList.as_view() , name='movie_list'),
    path('category/<str:category>', MovieCategory.as_view() , name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view() , name='movie_language'),
    path('search/', MovieSearch.as_view() , name='movie_search'),
    path('<slug:slug>', MovieDetail.as_view() , name='movie_detail'),
    path('year/<int:year>', MovieYear.as_view() , name='movie_year'),
]

