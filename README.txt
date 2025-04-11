AutoCreatorX - Deployment Guide

1. Prerequisites:
   - Python 3.9+
   - pip install streamlit openai

2. How to Run Locally:
   - Save files in a folder
   - Open terminal inside folder
   - Run: streamlit run app.py

3. Deploy for Free:
   a. Go to https://share.streamlit.io
   b. Connect GitHub or upload project ZIP
   c. Launch & share your app

Secrets Setup:
- Create `.streamlit/secrets.toml`
- Add your OpenAI API key like:
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxx"

Next Up:
- Add auto-video creation
- Add YouTube auto-upload