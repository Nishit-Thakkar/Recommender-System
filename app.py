import pickle
import streamlit as st
import requests
import pandas as pd

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
    recommended_movie_homeage = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_homeage.append(movies.iloc[i[0]].homepage)

    return recommended_movie_names,recommended_movie_posters,recommended_movie_homeage


st.header('Movie Recommender System By Nishit Thakkar')
movies_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_homeage = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        url=recommended_movie_homeage[0]
        if pd.isna(url):
            st.markdown("Movie Link is not available")
        else:
            st.markdown("Movie Link [link](%s)" % url)
        
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        url=recommended_movie_homeage[1]
        if pd.isna(url):
            st.markdown("Movie Link is not available")
        else:
            st.markdown("Movie Link [link](%s)" % url)

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        url=recommended_movie_homeage[2]
        if pd.isna(url):
            st.markdown("Movie Link is not available")
        else:
            st.markdown("Movie Link [link](%s)" % url)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        url=recommended_movie_homeage[3]
        if pd.isna(url):
            st.markdown("Movie Link is not available")
        else:
            st.markdown("Movie Link [link](%s)" % url)
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        url=recommended_movie_homeage[4]
        if pd.isna(url):
            st.markdown("Movie Link is not available")
        else:
            st.markdown("Movie Link [link](%s)" % url)

url = "https://drive.google.com/file/d/1k1-NGrQOzMWZbmmkS4FKRSuV4_8-aJM3/view?usp=sharing"
st.write("My Resume :- [link](%s)" % url)

# st.markdown("check out this [link](%s)" % url)



