import streamlit as st
from rag import generate_answer, process_urls

# Set page config
st.set_page_config(page_title="Smart URL Answer Bot", page_icon="🔗", layout="wide")

# Inject custom styles
st.markdown("""
    <style>
        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #a3e4d7;
            padding: 2rem 1rem 2rem 1rem;
            height: 100vh;
        }

        /* Remove sidebar white padding */
        .css-6qob1r.e1fqkh3o3 {
            padding: 0 !important;
        }

        /* Sidebar text */
        .css-ng1t4o, .css-1v0mbdj {
            color: black !important;
        }

        /* Sidebar input fields */
        .stTextInput input {
            background-color: #a2d9ce;
            border: none;
            border-radius: 8px;
            padding: 0.5rem;
        }

        /* Sidebar button */
        .stButton > button {
            background-color: #45b39d;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            padding: 0.5rem 1rem;
        }

        .stButton > button:hover {
            background-color: #16a085;
        }

        /* Main area background */
        .block-container {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
        }

        /* Title and headings */
        h1 {
            color: #a3e4d7 !important;
        }

        h2, h3, h4, h5 {
            color: #000000;
        }

        /* Answer Box */
        .answer-box {
            background-color: #a2d9ce;
            padding: 1rem;
            border-radius: 12px;
            color: #4b0f2f;
            font-weight: 500;
            font-size: 1rem;
        }

        /* Links */
        .stMarkdown a {
            color: #b80068;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("Your Smart URL Answer Bot")
st.markdown("Ask questions based on content from your favorite web pages.")

# Sidebar Inputs
st.sidebar.header("📥 Enter URLs to Process")
url1 = st.sidebar.text_input("🔗 URL 1")
url2 = st.sidebar.text_input("🔗 URL 2")
url3 = st.sidebar.text_input("🔗 URL 3")

status_placeholder = st.empty()

# Process Button
if st.sidebar.button("🚀 Process URLs"):
    urls = [url for url in (url1, url2, url3) if url.strip()]
    if not urls:
        status_placeholder.error("⚠️ Please enter at least one valid URL.")
    else:
        for status in process_urls(urls):
            status_placeholder.success(f"✅ {status}")

# Divider
st.markdown("---")

# Ask Question Section
st.markdown("### 💬 Ask a Question")
query = st.text_input("Type your question here and press Enter:")


       
if query:
    try:
        answer, sources = generate_answer(query)
        st.success("✅ Answer Generated!")

        st.markdown("### 🧠 Answer")
        st.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)

        if sources:
            st.markdown("### 📚 Sources")
            for source in sources.split("\n"):
                st.write(source)

    except RuntimeError:
        status_placeholder.error("⚠️ You must process the URLs first before asking a question.")