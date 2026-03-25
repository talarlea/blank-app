import streamlit as st

st.title("Mahna Mahna")
st.write("You have been Bamboozled!")

# Auto-play the YouTube video (muted to satisfy autoplay policies in browsers)
video_id = "QTXyXuqfBLA"
embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&mute=1&controls=1"

st.markdown(
    f"<iframe width=\"100%\" height=\"480\" src=\"{embed_url}\" frameborder=\"0\" allow=\"autoplay; encrypted-media; picture-in-picture\" allowfullscreen></iframe>",
    unsafe_allow_html=True,
)

