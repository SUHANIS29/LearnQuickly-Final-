
import streamlit as st
import requests

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📚",
    layout="centered"
)

st.markdown("""
<style>
    .main {
        background-color: #0E0126;
        color: #E9ECEF;
    }
    .stButton button {
        background-color: #6A0DAD;
        color: white;
        border-radius: 20px;
    }
    .stTextArea textarea {
        background-color: #2B0E44;
        color: #E9ECEF;
        border: 1px solid #9370DB;
    }
    h1, h2, h3 {
        color: #9370DB;
    }
    div[data-testid="stSlider"] [role="slider"] {
        background-color: #8A2BE2 !important;
        border-radius: 50%;
    }
    div[data-testid="stSlider"] [role="slider"]::before {
        background-color: transparent !important;
    }
    div[data-testid="stDownloadButton"] button {
        background-color: #4B0082;
        color: white;
        border-radius: 20px;
    }
    div.block-container {
        padding-top: 2rem;
    }
    .css-18e3th9 {
        padding-top: 2rem;
    }
            .title {
            font-size: 2.5rem;
            font-weight: 600;
            background: linear-gradient(90deg, #D13F77, #F68D2E);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }
         .nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(13, 2, 33, 0.9);
            padding: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 3px 10px rgba(209, 63, 119, 0.8);
            backdrop-filter: blur(10px);
            z-index: 1000;
        }
        .nav a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            font-weight: 500;
            transition: color 0.3s ease;
        }
        .nav a:hover {
            color: #D13F77;
            text-shadow: 0 0 10px #D13F77;
        }
</style>
""", unsafe_allow_html=True)
API_URL=""
HEADERS={}

def summarize_text(input_text, min_length, max_length):
    payload = {
        "inputs": input_text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length,
            "do_sample": False,
        },
    }
    
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    if response.status_code == 200:
        try:
            return response.json()[0]["summary_text"]
        except (KeyError, IndexError):
            return "Error: Unexpected API response format."
    else:
        return f"API Error {response.status_code}: {response.text}"

def create_text_file(summary_text):
    file_name = "summarized_text.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("Summarized Text:\n\n")
        file.write(summary_text)
    return file_name

st.markdown("""
<div class="nav">
    <div><a href="#"> Home</a></div>
    <div>
        <a href="#">About</a>
        <a href="#">Explore</a>
        <a href="#" class="logout-btn">Logout</a>
    </div>
</div>
""", unsafe_allow_html=True)
# st.title("✨Text Summarizer ✨")
st.markdown("<h1 class='title'>✨ Text Summarizer ✨</h1>", unsafe_allow_html=True)
st.markdown(" Get precise and concise summary")

# st.markdown("Enter Your Text")
text_input = st.text_area("Enter Your Text", height=200)


max_length = st.slider("Maximum Summary Length", min_value=50, max_value=300, value=150, step=10)
min_length = max(20, max_length // 2)

st.markdown("---")

summary = None 

if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("wait for it summary is being generated..."):
            summary = summarize_text(text_input, min_length, max_length)
            st.markdown("✨Generated Summary")
            st.markdown(f'<div style="background-color: #2B0E44; padding: 15px; border-radius: 10px; border: 1px solid #8A2BE2;">{summary}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some text.")

if summary:
    txt_file = create_text_file(summary)
    
    with open(txt_file, "rb") as file:
        st.download_button(
            label="📥Download Summary as Txt File",
            data=file,
            file_name="txt_summary.txt",
            mime="text/plain",
        )