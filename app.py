import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="THIBAZA Research Profile",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Custom Styling ---
st.markdown(
    """
    <style>
    body {
        background-color: #f8f5fa;
    }
    .main {
        background-color: #fdfdff;
        border-radius: 12px;
        padding: 20px;
    }
    h1, h2, h3 {
        color: #a678c2; /* soft lavender purple */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title Section ---
st.title("🌸 THIBAZA’s Research & Dreams 🌸")
st.write("Welcome to my profile page — a mix of science, dreams, and aesthetics.")

# --- Anime/Cartoon Image Section ---
st.header("🎨 Aesthetic Vibes")
st.image(
    "https://i.pinimg.com/564x/8a/3f/9d/8a3f9d8a3f9d8a3f.jpg", 
    caption="Dreamy lavender-inspired art"
)

# --- About Section ---
with st.expander("✨ About Me"):
    st.write("""
    Hi, I'm THIBAZA MLAMBO — I have recently completed my BSc degree in Computer Science & Biochemistry at the University of Fort Hare.
    I am now aspiring to pursue Honours in Computer Science, hoping to deepen my knowledge 
    and continue growing in both technical and research fields.
    
    I love nature, music, and quiet moments, but I also dream big about the future.
    I’m still exploring where my path will lead, but I enjoy learning and sharing knowledge..
    """)

# --- Research Section ---
st.header("🔬 My Research Interests")
st.write("""
- **Computer Science**: Systems analysis, databases, operating systems.
- **Biochemistry**: Exploring molecular processes and scientific problem-solving.
- **Data Analysis**: Using Pandas and Python to uncover insights.
""")

# --- Dreams Section ---
with st.expander("🌙 My Dreams"):
    st.write("""
    I have many dreams — some clear, some still forming.
    I want to grow, explore opportunities, and find my unique place in the world.
    """)

# --- Fun Section ---
st.header("🎶 Music & Peace")
st.write("I love listening to music, but I also enjoy peace and quiet.")

# Embed YouTube player for Broken Trails - Hate Me All You Want
st.markdown(
    """
    <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/kuqlDCMPrGg" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
    encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
    </iframe>
    """,
    unsafe_allow_html=True
)

# --- Nature Section ---
st.header("🌿 Nature & Aesthetics")
st.image("sunset.jpg", caption="Calm nature vibes kissed by sunset", width=400)



# --- Contact Section ---
st.sidebar.header("📬 Connect with Me")
st.sidebar.write("Email: thibazamlambo@gmail.com")







