import google.generativeai as genai
from django.conf import settings
from .models import Movie
import json
import logging

logger = logging.getLogger(__name__)


class GeminiMovieAI:
    def __init__(self):
        """Initialize Gemini AI"""
        try:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            # Try gemini-1.5-flash first (fastest and free)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            # Test the model with a simple request
            test_response = self.model.generate_content("Hello")
            logger.info("Gemini AI initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Gemini: {e}")
            # Try fallback model
            try:
                self.model = genai.GenerativeModel('gemini-1.5-pro')
                logger.info("Using Gemini 1.5 Pro as fallback")
            except Exception as e2:
                logger.error(f"Fallback model also failed: {e2}")
                self.model = None

    def get_movies_context(self):
        """Get all movies data for context"""
        movies = Movie.objects.all()
        movies_data = []

        for movie in movies:
            movies_data.append({
                'id': movie.id,
                'title': movie.title,
                'director': movie.director,
                'actors': movie.four_main_actors,
                'year': movie.year_of_release,
                'description': movie.description,
                'rating': round(movie.average_rating, 1) if movie.average_rating > 0 else 'No ratings'
            })

        return movies_data

    def get_movie_recommendations(self, user_message):
        """Get AI response and movie recommendations"""
        if not self.model:
            return "Sorry, the AI service is currently unavailable.", []

        try:
            # Get movies data
            movies_data = self.get_movies_context()

            # Create prompt for Gemini
            prompt = f"""
            You are a helpful movie recommendation assistant. You have access to a movie database with the following movies:

            {json.dumps(movies_data, indent=2)}

            User asked: "{user_message}"

            Please provide a helpful response and recommend relevant movies from the database above. 

            Format your response as follows:
            1. Give a friendly conversational response
            2. If recommending movies, mention them by title and explain why
            3. Include relevant details like director, year, rating, and brief description
            4. Be conversational and helpful

            At the end of your response, include a JSON array of recommended movie IDs like this:
            RECOMMENDED_IDS: [1, 5, 8]

            If no specific movies to recommend, use: RECOMMENDED_IDS: []
            """

            # Get response from Gemini
            response = self.model.generate_content(prompt)
            ai_response = response.text

            # Extract recommended movie IDs
            recommended_movies = self.extract_recommended_movies(ai_response, movies_data)

            # Clean up response (remove the JSON part)
            clean_response = ai_response.split('RECOMMENDED_IDS:')[0].strip()

            return clean_response, recommended_movies

        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            return "I'm having trouble processing your request right now. Please try again.", []

    def extract_recommended_movies(self, ai_response, movies_data):
        """Extract recommended movie objects from AI response"""
        try:
            # Find the recommended IDs in the response
            if 'RECOMMENDED_IDS:' in ai_response:
                ids_part = ai_response.split('RECOMMENDED_IDS:')[1].strip()
                # Extract the JSON array
                import re
                ids_match = re.search(r'\[(.*?)\]', ids_part)
                if ids_match:
                    ids_str = ids_match.group(1)
                    if ids_str.strip():
                        movie_ids = [int(id.strip()) for id in ids_str.split(',') if id.strip().isdigit()]
                        # Get movie objects
                        return list(Movie.objects.filter(id__in=movie_ids))

            return []
        except Exception as e:
            logger.error(f"Error extracting recommendations: {e}")
            return []