import streamlit as st
import pickle
import pandas as pd
import requests

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            footer:after{
            content: '@AkshatJhalani';
            display: block;
            position: relative;
            color: tomato
            }
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def fetchPoster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cd4fc23ab51e7087822861ef0e51367a&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movieIndex = movies[movies['title'] == movie].index[0]
    distances = similarity[movieIndex]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    recPosters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        #fetch poster using the api
        recommendations.append(movies.iloc[i[0]].title)
        recPosters.append(fetchPoster(movie_id))
    return recommendations, recPosters

moviesDict = pickle.load(open('moviesDict.pkl','rb'))
movies = pd.DataFrame(moviesDict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender! 🍿')

selectedMovie = st.selectbox(
    'Select a movie to get recommendations: ',
    movies['title'].values)

if st.button('Recommend'):
    names,poster = recommend(selectedMovie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
