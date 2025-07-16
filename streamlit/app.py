import streamlit as st
import requests
import time
import random
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="Viral Tweet Reflector", page_icon="🧠", layout="centered")

# Custom CSS for a beautiful background and enhanced elements
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="st-emotion-cache"] {
        font-family: 'Poppins', sans-serif;
        color: #333;
    }

    /* --- General Layout and Background --- */
    .stApp {
        background: linear-gradient(135deg, #f0f2f5 0%, #e0e5ec 100%);
        background-size: cover;
        animation: gradientAnimation 10s ease infinite alternate;
    }

    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    /* --- Main Container Styling --- */
    /* Target the main block container where content sits */
    .css-1dp5vir.e1ts377r1 {
        max-width: 700px; /* NEW: Limit max width for a lighter feel */
        margin: 2em auto; /* Center the container with auto margins */
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2.5em; /* Slightly reduced padding */
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08); /* Softer, slightly smaller shadow */
        border: 1px solid rgba(220, 220, 220, 0.5);
        animation: fadeIn 1s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* --- Titles and Subtitles --- */
    .main-title {
        text-align: center;
        font-size: 3em; /* Slightly smaller for balance */
        font-weight: 700;
        margin-bottom: 0.1em;
        color: #2c3e50;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.03); /* Lighter text shadow */
    }
    .subtitle {
        text-align: center;
        font-size: 1.3em; /* Slightly smaller */
        color: #555;
        margin-bottom: 1.8em; /* Adjusted margin */
        font-weight: 300;
    }

    /* --- Input Area --- */
    .stTextArea label {
        font-size: 1.1em; /* Slightly smaller */
        font-weight: 600;
        color: #444;
        margin-bottom: 0.4em;
    }
    .stTextArea textarea {
        border: 1px solid #c0c0c0;
        border-radius: 10px;
        padding: 0.9em; /* Slightly reduced padding */
        background-color: #f8f9fa;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.03); /* Softer inner shadow */
        transition: all 0.3s ease;
    }
    .stTextArea textarea:focus {
        border-color: #6a11cb;
        box-shadow: 0 0 0 0.2rem rgba(106, 17, 203, 0.2); /* Lighter glow effect */
        outline: none;
    }

    /* --- Button Styling --- */
    .stButton > button {
        background-image: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        font-size: 1.1em; /* Slightly smaller */
        font-weight: 600;
        padding: 0.7em 1.8em; /* Slightly reduced padding */
        border: none;
        border-radius: 10px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); /* Softer shadow */
        transition: all 0.3s ease;
        cursor: pointer;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px); /* Smaller lift effect */
        box-shadow: 0 10px 18px rgba(0, 0, 0, 0.25); /* Softer hover shadow */
    }
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    /* --- Improved Tweet Display --- */
    .stMarkdown .st-emotion-cache-nahz7x.e1nzilvr4 { /* Target the subheader for improved tweet */
        color: #1a5e20; /* Keep green for success */
        font-size: 1.6em; /* Slightly smaller */
        font-weight: 600;
        margin-top: 1.5em;
        margin-bottom: 0.8em;
        border-bottom: 2px solid #d4edda; /* Lighter underline */
        padding-bottom: 0.3em;
    }
    .tweet-box {
        border: 1px solid #d4edda;
        border-radius: 12px;
        padding: 1.2em; /* Slightly reduced padding */
        background-color: #eaf7ed;
        font-size: 1.1em; /* Slightly smaller font */
        font-weight: 500;
        color: #1a5e20;
        box-shadow: 0 3px 10px rgba(0, 128, 0, 0.08); /* Softer green shadow */
        line-height: 1.6; /* Slightly increased line height for readability */
        white-space: pre-wrap;
        word-wrap: break-word;
    }

    /* --- Expander for Original Tweet --- */
    .stExpander {
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        background-color: #fcfcfc; /* Lighter background */
        margin-top: 1em;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05); /* Softer shadow */
    }
    .stExpander details {
        padding: 0.7em 1em; /* Reduced padding */
        font-weight: 500;
        color: #555;
    }
    .stExpander div[data-baseweb="accordion"] {
        padding: 0.4em 1em; /* Reduced padding */
        background-color: #fafafa;
        border-top: 1px solid #eee;
    }
    .stExpander .markdown-text-container p { /* Style for content inside expander */
        font-size: 0.95em;
        line-height: 1.5;
        color: #666;
    }

    /* --- AI Feedback Summary --- */
    .stMarkdown h4 { /* Target general h4 for the summary title */
        color: #2c3e50;
        margin-top: 1.5em;
        margin-bottom: 0.8em;
        font-weight: 600;
        font-size: 1.4em; /* Match subheader size */
        border-bottom: 1px solid #ddd; /* Subtle underline */
        padding-bottom: 0.2em;
    }

    /* Individual Badge Styling */
    .stMarkdown div[style*="display: flex"] span {
        font-size: 0.9em; /* Smaller badges */
        padding: 0.4em 0.8em; /* Adjusted padding */
        border-radius: 6px; /* Slightly smaller border radius */
        font-weight: 600;
        margin: 0.3em; /* Reduced margin */
        box-shadow: 0 2px 5px rgba(0,0,0,0.05); /* Lighter shadow for badges */
    }

    /* --- Detailed Agent Feedback Box --- */
    [data-testid="stInfo"] {
        background-color: #e0f2f7;
        border-left: 5px solid #2196f3;
        border-radius: 10px;
        padding: 1.2em 1.5em; /* Slightly adjusted padding */
        margin-top: 1.5em;
        box-shadow: 0 3px 10px rgba(33, 150, 243, 0.08); /* Softer blue shadow */
    }
    [data-testid="stInfo"] .st-emotion-cache-1f87s81.e1nzilvr1 {
        font-size: 1em; /* Slightly smaller */
        line-height: 1.7; /* Increased line height for feedback readability */
        color: #333;
    }

    /* --- Footer --- */
    .footer {
        text-align: center;
        color: #888;
        margin-top: 2.5em; /* Slightly reduced margin */
        padding-top: 1em;
        border-top: 1px solid #eee;
        font-size: 0.85em; /* Slightly smaller font */
    }

    /* --- Spinner customization --- */
    .stSpinner > div > div {
        color: #6a11cb;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# 🎯 Page Header (Using custom classes)
st.markdown(
    """
    <div class='main-title'>🧠 Viral Tweet Reflector</div>
    <div class='subtitle'>Improve your tweet with AI-powered feedback & rewriting.</div>
    """,
    unsafe_allow_html=True
)

# ✍️ User Input
user_tweet = st.text_area("Write your tweet here ✍️", height=150, placeholder="e.g. LangChain vs LangGraph: Which one is better for agents?")

# 🌈 Improvement button
if st.button("🚀 Improve Tweet"):
    if not user_tweet.strip():
        st.warning("Please enter a tweet first.")
    else:
        with st.spinner("🔍 Reflecting on your tweet... This might take a moment as the AI brainstorms..."):
            try:
                response = requests.post(
                f"{BACKEND_URL}/improve_tweet",
                json={"tweet": user_tweet}
                )
                if response.status_code == 200:
                    result = response.json()

                    # 🎯 Display Results
                    st.markdown("---")
                    st.subheader("✅ Improved Tweet") # This uses Streamlit's default subheader but matches its styling with CSS
                    st.markdown(
                        f"<div class='tweet-box'>{result['improved_tweet']}</div>",
                        unsafe_allow_html=True
                    )

                    # Optional: Display Original Tweet with expander
                    with st.expander("🔙 Show Original Tweet"):
                        st.markdown(f"> {user_tweet}")

                    # 📊 Quick Ratings (Dynamic if possible, otherwise randomized for demo)
                    st.markdown("#### 📈 AI Feedback Summary") # This uses Streamlit's default h4 but matches its styling with CSS

                    st.markdown(
                        f"""
                        <div style="display: flex; justify-content: center; flex-wrap: wrap; margin-top: 1em;">
                            <span style="background-color: #d4edda; color: #1a5e20; padding: 0.5em 1em; border-radius: 8px; font-weight: 600; margin: 0.5em;">🔥 Viral Potential: {random.randint(7, 9)}/10</span>
                            <span style="background-color: #e0f2f7; color: #2196f3; padding: 0.5em 1em; border-radius: 8px; font-weight: 600; margin: 0.5em;">🧠 Clarity: {random.randint(8, 10)}/10</span>
                            <span style="background-color: #ffe0b2; color: #ff9800; padding: 0.5em 1em; border-radius: 8px; font-weight: 600; margin: 0.5em;">🎯 Style: {random.randint(7, 9)}/10</span>
                        </div>
                        """, unsafe_allow_html=True
                    )

                else:
                    st.error(f"❌ Error from backend: Status Code {response.status_code}")
                    st.json(response.json())
            except requests.exceptions.ConnectionError:
                st.error("🔌 Could not connect to the FastAPI backend. Please ensure it's running at `http://localhost:8000`.")
            except Exception as e:
                st.error(f"An unexpected error occurred: `{e}`")

# Footer
st.markdown(
    "<div class='footer'>Made with ❤️ by Saketh • Powered by LangGraph + FastAPI</div>",
    unsafe_allow_html=True
)
