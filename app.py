import streamlit as st
from recommendation_system import recommend_songs

st.title("Music Recommendation System")
st.write("Get recommendations based on speed or a song name!")

song_name = st.text_input("Enter a song name (optional):")
speed_category = st.selectbox("Select speed category:", ["", "Slow", "Medium", "Fast"])

if st.button("Recommend Songs"):
    recommendations = recommend_songs(song_name=song_name, speed_category=speed_category)
    if isinstance(recommendations, str):
        st.error(recommendations)
    else:
        st.write("Recommended Songs:")
        st.dataframe(recommendations)
