# 🎬 MovieLib - Django Movie Library with AI Assistant

A comprehensive movie library management system built with Django, featuring a dark IMDb-style interface for browsing movies, reading reviews, managing content, and an intelligent AI-powered movie recommendation system.

## ✨ Features

### 🎭 **Movie Management**
- Browse movies in an elegant grid layout with hover effects
- View detailed movie information with posters and ratings
- Click any movie to see full details, cast, and user reviews
- Admin-only movie addition with secure upload forms
- Movie posters with automatic scaling and fallback images
- Average rating calculations displayed with star ratings

### ⭐ **Review System**
- User reviews with 1-5 star ratings
- Authenticated user review submission
- Average rating calculations
- Review moderation capabilities

### 🤖 **AI Movie Assistant**
- **Gemini AI Integration**: Powered by Google's Gemini AI
- **Smart Recommendations**: Get personalized movie suggestions
- **Natural Language Queries**: Ask questions in plain English
- **Context-Aware Responses**: AI knows your movie collection
- **Interactive Chat Interface**: Real-time conversation with movie bot
- **Movie Discovery**: Find films based on genre, mood, director, or actors

### 🎨 **User Interface**
- Dark theme with IMDb-inspired design
- Responsive design for all devices
- Smooth animations and hover effects
- Professional admin dashboard
- Modern chat interface with typing indicators

### 🔐 **Authentication & Security**
- Secure user registration and login
- Password hashing with Django's built-in tools
- Admin-only access to management features
- CSRF protection on all forms
- Session-based chat history for authenticated users

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 4.0+
- Pillow (for image handling)
- Google Gemini API Key (for AI features)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd djangoProjectBackendCourse/movies
   ```

2. **Create virtual environment**
   ```bash
   python -m venv movielib_env
   source movielib_env/bin/activate  # On Windows: movielib_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow google-generativeai
   ```

4. **Configure Gemini AI**
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Add to your `settings.py`:
   ```python
   GEMINI_API_KEY = 'your-gemini-api-key-here'
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the application**
   - Main site: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`
   - AI Chat: `http://127.0.0.1:8000/chat/`

## 🎯 Models

### Movie Model
```python
class Movie(models.Model):
    poster = models.ImageField(upload_to='movie_images/')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    director = models.CharField(max_length=100)
    four_main_actors = models.CharField(max_length=100)
    year_of_release = models.PositiveIntegerField()
    
    @property
    def average_rating(self):
        # Calculates average rating from reviews
```

### Review Model
```python
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.PositiveIntegerField()  # 1-5 stars
    review_date = models.DateTimeField(auto_now_add=True)
```

### AI Chat Models
```python
class ChatSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
```

## 🛠️ Key Features Implementation

### 🎬 **Movie Library**
- **Grid Layout**: Responsive card-based design
- **Hover Effects**: Smooth animations and overlays
- **Image Handling**: Automatic poster scaling and fallback
- **Rating Display**: Star-based rating system

### ⭐ **Review System**
- **Star Ratings**: 1-5 star selection with visual feedback
- **User Authentication**: Only logged-in users can review
- **Average Calculations**: Real-time rating aggregation
- **Review Display**: Clean, readable review cards

### 🤖 **AI Movie Assistant**
- **Gemini Integration**: Uses Google's powerful AI models
- **Context Awareness**: AI knows your entire movie collection
- **Smart Parsing**: Understands natural language movie queries
- **Visual Recommendations**: Shows movie cards with ratings
- **Chat History**: Saves conversations for logged-in users
- **Error Handling**: Graceful fallbacks and user-friendly messages

### 🔐 **Admin Dashboard**
- **Access Control**: Staff-only access with decorators
- **Statistics**: Real-time movie and review counts
- **CRUD Operations**: Add movies with validation
- **Quick Actions**: Easy navigation to key features

### 🎨 **UI/UX Design**
- **Dark Theme**: IMDb-inspired color scheme (#0f0f0f, #1a1a1a)
- **Yellow Accents**: Consistent #f5c518 highlight color
- **Responsive Design**: Mobile-first approach
- **Smooth Animations**: CSS transitions and transforms
- **Modern Chat UI**: WhatsApp-inspired chat interface

## 🔧 URL Patterns

```python
# Main URLs
/                           # Home page (redirects to library)
/library/                   # All movies page
/library/movie/<id>/        # Movie detail page
/library/reviews/           # All reviews page
/library/movie/<id>/reviews/ # Individual movie reviews
/dashboard/                 # Admin dashboard (staff only)
/add-movie/                 # Add movie form (staff only)
/chat/                      # AI movie chat assistant
/chat/history/              # Chat history (authenticated users)
/login/                     # User login
/signup/                    # User registration
```

## 🤖 AI Features

### **Movie Recommendations**
Ask the AI assistant questions like:
- "What are the highest rated movies?"
- "Show me action movies from the 2000s"
- "I want something like Inception"
- "Recommend a good comedy"
- "What movies have Tom Hanks?"

### **Smart Context Understanding**
The AI understands:
- **Genres and themes**
- **Directors and actors**
- **Years and decades**
- **Ratings and popularity**
- **Mood and preferences**

### **Response Types**
- **Text recommendations** with explanations
- **Visual movie cards** with ratings and details
- **Curated lists** based on your query
- **Personalized suggestions** from your collection

## 🔒 Security Features

### Password Security
- Django's built-in password hashing (PBKDF2/Argon2)
- Password validation requirements
- Secure authentication using `UserCreationForm`

### Access Control
- `@staff_member_required` decorators for admin functions
- User authentication checks for review submissions
- CSRF protection on all forms
- API key security for Gemini AI

### File Upload Security
- Image validation for movie posters
- File size limitations
- Secure file storage in media directory

## 🎨 Styling Guide

### Color Palette
- **Background**: `#0f0f0f` (Primary dark)
- **Cards/Containers**: `#1a1a1a` (Secondary dark)
- **Borders**: `#333` (Dark gray)
- **Accent**: `#f5c518` (Golden yellow)
- **Text**: `#ffffff` (White), `#cccccc` (Light gray)
- **AI Elements**: Consistent with main theme

### Typography
- **Headers**: Bold, clean sans-serif
- **Body**: Readable 14-16px sizes
- **Chat**: Modern messaging-style fonts
- **Spacing**: Consistent 15-30px gaps

## 🚀 Deployment

### Environment Variables
```bash
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-domain.com
GEMINI_API_KEY=your-gemini-api-key
```

### Dependencies
```bash
pip install django pillow google-generativeai
```

### Static Files
```bash
python manage.py collectstatic
```

### Database
- Development: SQLite (default)



- **Django Framework** - For the robust backend foundation
- **Google Gemini AI** - For the powerful AI movie recommendations
- **IMDb** - Design inspiration for the dark theme


