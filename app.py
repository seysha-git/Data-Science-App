import streamlit as st
from streamlit_option_menu import option_menu

def navigation():
    pass
def title():
    st.set_page_config(layout="wide")
    st.title("Explore and interact with my ML projects")
    st.write("[Read more](https://github.com/seysha-git)")
    st.write('---')


def main():
    navigation()
    title()    
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=['Supervised learning', 'Unsupervised learning', 'Reinforcement learning'],
            orientation= 'horizontal'
        )

    if selected == 'Supervised learning':
        with st.container():
            st.write("##")
            col1, col2, col3 = st.columns(3, border=True)
            with col1:
                st.subheader("Spaceship Titanic Transported Prediction")
                st.page_link("pages/Titanic.py", label="Explore", icon="📄")
            with col2:
                st.subheader("Spaceship Titanic Transported Prediction")
                st.page_link("pages/Titanic.py", label="Explore", icon="📄")
            with col3:
                st.subheader("Spaceship Titanic Transported Prediction")
                st.page_link("pages/Titanic.py", label="Explore", icon="📄")
    elif selected == 'Unsupervised learning':
        with st.container():
            st.write("##")
            col1, col2, col3 = st.columns(3, border=True)
            with col1:
                st.subheader("Spaceship Titanic Transported Prediction")
                st.page_link("pages/Titanic.py", label="Explore", icon="📄")
            with col2:
                st.subheader("Spaceship Titanic Transported Prediction")
                st.page_link("pages/Titanic.py", label="Explore", icon="📄")
            with col3:
                st.subheader("Spaceship Titanic Transported Prediction")
                st.page_link("pages/Titanic.py", label="Explore", icon="📄")
    elif selected == 'Reinforcement learning':
        with st.container():
            st.write("##")
            col1, col2, col3 = st.columns(3, border=True)
            with col1:
                st.subheader("Spaceship Titanic Transported Prediction")
                st.page_link("pages/Titanic.py", label="Explore", icon="📄")
            with col2:
                st.subheader("Spaceship Titanic Transported Prediction")
                st.page_link("pages/Titanic.py", label="Explore", icon="📄")
            with col3:
                st.subheader("Spaceship Titanic Transported Prediction")
                st.page_link("pages/Titanic.py", label="Explore", icon="📄")



main()