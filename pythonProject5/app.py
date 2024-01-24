import streamlit as st
import pickle
import pandas as pd
import requests


def movie_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c29f6691541c75b79378a3871441e32a".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(movie_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'How would you like to contacted?',
    movies['title'].values
)
if st.button('Recommend movie'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.text(names[0])
    col1.image(posters[0])
    col2.text(names[1])
    col2.image(posters[1])
    col3.text(names[2])
    col3.image(posters[2])
    col4.text(names[3])
    col4.image(posters[3])
    col5.text(names[4])
    col5.image(posters[4])
