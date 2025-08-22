from django.urls import path
from .views import all_movies, movie_detail, all_reviews, movie_reviews, add_movie, dashboard, chat_page, chat_history
from django.conf import settings
from django.conf.urls.static import static

app_name="library"
urlpatterns = [
    path("all_movies/", all_movies, name="all_movies"),
    path("", all_movies, name="home"),
    path("<int:pk>/", movie_detail, name="movie_detail"),
    path('reviews/', all_reviews, name='all_reviews'),
    path('<int:pk>/reviews/', movie_reviews, name='movie_reviews'),
    path('add-movie/', add_movie, name='add_movie'),
    path('dashboard/', dashboard, name='dashboard'),
    path('chat/', chat_page, name='chat'),
    path('chat/history/', chat_history, name='chat_history'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)