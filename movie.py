import pickle
import time
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie_spinner
import requests
import bz2

img = Image.open('watching-a-movie.png')
st.set_page_config(page_title='MuviEra',layout='wide',page_icon=img)

hide_st_style = """
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #d85f25;">
  <a class="navbar-brand" href="http://127.0.0.1:8000/muviera" target="_blank"></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
Content Based Movie Recommendation System
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

def loadgifs(url : str ):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_wait_url= "https://assets9.lottiefiles.com/packages/lf20_f1qtk0oe.json"
lottie_wait = loadgifs(lottie_wait_url)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:18]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.title('Movie Recommendation System')
movies = pickle.load(open('movies.pkl','rb'))
ifile = bz2.BZ2File("similarity_index.pkl",'rb')
similarity = pickle.load(ifile)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)
st.write('You selected:', selected_movie)


if st.button('Show Recommendation'):                                                           
    with st_lottie_spinner(lottie_wait, key='wait'):
        time.sleep(4)
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 , col6, col7, col8 =  st.columns(8)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])

if st.button("Next"):
    with st_lottie_spinner(lottie_wait, key='wait'):
        time.sleep(4)
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 , col6, col7, col8 =  st.columns(8)
    with col1:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col2:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
    with col3:
        st.text(recommended_movie_names[10])
        st.image(recommended_movie_posters[10])
    with col4:
        st.text(recommended_movie_names[11])
        st.image(recommended_movie_posters[11])
    with col5:
        st.text(recommended_movie_names[12])
        st.image(recommended_movie_posters[12])
    with col6:
        st.text(recommended_movie_names[13])
        st.image(recommended_movie_posters[13])
    with col7:
        st.text(recommended_movie_names[14])
        st.image(recommended_movie_posters[14])
    with col8:
        st.text(recommended_movie_names[15])
        st.image(recommended_movie_posters[15])





