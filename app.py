import streamlit as st
import openai

# Securely load OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AutoCreatorX", layout="centered")
st.title("AutoCreatorX")
st.subheader("AI-Powered Content-to-Cash Generator")

st.markdown("### Step 1: Choose a Niche")
niche = st.selectbox("Pick a niche:", [
    "Brain Boost Hacks", 
    "Fat Loss Secrets", 
    "Passive Income Ideas", 
    "Spiritual Awakening", 
    "Sarkari Job Scams"
])

st.markdown("### Step 2: One Click to Auto Generate Everything")

def generate_script(niche):
    prompt = f"Create a viral YouTube Shorts script in the niche of '{niche}'. Format: HOOK, VALUE, CTA."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

if st.button("Start Automation"):
    with st.spinner("Generating with AI..."):
        script = generate_script(niche)
        title = f"3 {niche} That Actually Work | AI-Generated Hacks"
        description = f"Boost your {niche.lower()} using science-backed AI tools. Includes affiliate tools for smarter living. #MindFuelByVidyut"

        st.success("✅ Content Generated!")
        st.markdown("### ✨ AI Script")
        st.code(script, language='markdown')
        st.markdown("### 🎬 YouTube Title")
        st.write(title)
        st.markdown("### 📝 YouTube Description")
        st.write(description)
        st.markdown("### 🔗 Affiliate Links")
        st.markdown("""
- [Amazon Health Product](https://www.amazon.in/dp/B09YH8WGRN?tag=healthboostpr-20)  
- [Digistore Brain Hack](https://www.digistore24.com/redir/428393/healthboostpro-20/)
""")