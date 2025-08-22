from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .forms import MovieForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import uuid
from .ai_service import GeminiMovieAI
from .models import ChatSession, ChatMessage

movie_ai = GeminiMovieAI()


def chat_page(request):
    """Display the chat page"""
    if request.method == 'POST':
        # Handle form submission
        user_message = request.POST.get('message', '').strip()

        if user_message:
            try:
                # Get AI response
                ai_response, recommended_movies = movie_ai.get_movie_recommendations(user_message)

                # Save chat message for logged in users
                if request.user.is_authenticated:
                    session_id = str(uuid.uuid4())
                    chat_session = ChatSession.objects.create(
                        session_id=session_id,
                        user=request.user
                    )
                    ChatMessage.objects.create(
                        session=chat_session,
                        message=user_message,
                        response=ai_response
                    )

                context = {
                    'total_movies': Movie.objects.count(),
                    'total_reviews': Review.objects.count(),
                    'user_message': user_message,
                    'ai_response': ai_response,
                    'recommended_movies': recommended_movies,
                }

            except Exception as e:
                context = {
                    'total_movies': Movie.objects.count(),
                    'total_reviews': Review.objects.count(),
                    'error_message': f"Sorry, there was an error: {str(e)}",
                }
        else:
            context = {
                'total_movies': Movie.objects.count(),
                'total_reviews': Review.objects.count(),
                'error_message': "Please enter a message.",
            }
    else:
        # GET request - show empty chat
        context = {
            'total_movies': Movie.objects.count(),
            'total_reviews': Review.objects.count(),
        }

    return render(request, 'library/chat.html', context)

@login_required
def chat_history(request):
    """View chat history for logged in users"""
    sessions = ChatSession.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'chat_history.html', {'sessions': sessions})



@staff_member_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library:dashboard')
    else:
        form = MovieForm()

    return render(request, 'library/add_movie.html', {'form': form})


@staff_member_required
def dashboard(request):
    context = {
        'total_movies': Movie.objects.count(),
        'total_reviews': Review.objects.count(),
        'total_users': User.objects.count(),
    }
    return render(request, 'library/dashboard.html', context)


def all_movies(request):
    movies = Movie.objects.all()
    return render(request, "library/all_movies.html", {"movies":movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST' and request.user.is_authenticated:
        # Handle review submission
        Review.objects.create(
            movie=movie,
            reviewer_name=request.POST['reviewer_name'],
            review_text=request.POST['review_text'],
            rating=int(request.POST['rating'])
        )
        return redirect('library:movie_detail', pk=movie.pk)

    return render(request, 'library/movie_detail.html', {'movie': movie})


def all_reviews(request):
    movies_with_reviews = Movie.objects.filter(reviews__isnull=False).distinct().prefetch_related('reviews')

    return render(request, 'library/all_reviews.html', {
        'movies': movies_with_reviews,
        'movies_with_reviews_count': movies_with_reviews.count()
    })

def movie_reviews(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'library/movie_reviews.html', {'movie': movie})
