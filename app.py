import streamlit as st
import pickle
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the saved model
try:
    with open('movie_recommender.sav', 'rb') as f:
        model_data = pickle.load(f)
    movies_data = model_data['movies_data']
    similarity = model_data['similarity']
except FileNotFoundError:
    st.error("Error: 'movie_recommender.sav' not found. Make sure it's in the same directory as app.py.")
except Exception as e:
    st.error(f"An error occurred: {e}")

def recommend_movies(movie_name):
    find_close_match = difflib.get_close_matches(movie_name, movies_data['title'].tolist())
    if find_close_match:
        close_match = find_close_match[0]
    else:
        return ["No close matches found. Please check the movie name."]
    
    movie_index = movies_data[movies_data.title == close_match].index[0]
    similarity_score = list(enumerate(similarity[movie_index]))
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
    
    recommended_movies = []
    for movie in sorted_similar_movies[1:11]:
        index = movie[0]
        title_from_index = movies_data[movies_data.index==index]['title'].values[0]
        recommended_movies.append(title_from_index)
    
    return recommended_movies

def home_page():
    st.title("🎬 Movie Recommendation System")
    st.write("Welcome to the Movie Recommendation System!")
    
    st.header("About the Project")
    st.write("""
    This project uses machine learning to recommend movies based on your preferences. 
    It employs natural language processing and cosine similarity to find movies that are similar to the one you input.
    """)
    
    st.header("How it Works")
    st.write("""
    1. Enter the name of a movie you like
    2. Our system finds similar movies based on genres, keywords, cast, and more
    3. Get a list of 10 movie recommendations
    """)
    
    st.header("About Me")
    st.write("""
    Hi, I'm Sujit Varma Kalidindi, a passionate data scientist and movie enthusiast. 
    I created this project to combine my love for cinema with my skills in machine learning.
    
    - 🎓 Education: B.Tech in Information Technology
    - 💼 Current Role: Student
    - 📧 Contact: ksujivarma2003@gmail.com
    """)

def recommendation_page():
    st.title("🎥 Get Movie Recommendations")
    
    movie_name = st.text_input('Enter a movie name you like:')
    
    if st.button('Get Recommendations'):
        if movie_name:
            with st.spinner('Finding great movies for you...'):
                recommendations = recommend_movies(movie_name)
            st.success('Here are your recommendations!')
            for i, movie in enumerate(recommendations, 1):
                st.write(f"{i}. {movie}")
        else:
            st.warning('Please enter a movie name.')

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Get Recommendations"])
    
    if page == "Home":
        home_page()
    elif page == "Get Recommendations":
        recommendation_page()

if __name__ == "__main__":
    st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
    main()
