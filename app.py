# app.py
import streamlit as st
from logic import get_roast_and_fix
import time


st.set_page_config(page_title="Code Roaster", page_icon="😈")

st.title("The Code Roaster")
st.markdown("""
    **Dare to paste your code?** I will judge your syntax, your logic, and your life choices. 
    But if you cry, I might help you fix it.
""")

st.sidebar.header("Choose Your Judge")
persona = st.sidebar.selectbox(
    "Who is reviewing your code?",
    [
        "A Burned-out Senior Engineer (Sarcastic & Mean)",
        "A Medieval Peasant (Confused by technology)",
        "A Gen-Z TikToker (Uses slang, hates old tech)",
        "A Noir Detective (Gritty, dramatic)"
    ]
)

user_code = st.text_area("Paste your code here:", height=200, placeholder="def spaghetti_code(): ...")

if st.button("Judge Me"):
    if not user_code:
        st.warning("Paste some code first. I can't roast nothingness.")
    else:
        with st.spinner("No offense in advance just facts!!"):

            data = get_roast_and_fix(user_code, persona)
            
            if "critiques" in data:
                reviews = data["critiques"]
                
                fatal_errors = [r for r in reviews if r.get("fatal") is True]
                
                if fatal_errors:
                    placeholder = st.empty() 
                    
                    explosion_url = "https://media.giphy.com/media/HhTXt43pk1I1W/giphy.gif" 
                    
                    with placeholder.container():
                        st.markdown("<h1 style='text-align: center; color: red;'>💥 CRITICAL FAILURE DETECTED 💥</h1>", unsafe_allow_html=True)
                        st.image(explosion_url, use_container_width=True)
                        
                        # st.audio("explosion_sound.mp3") 
                    
                    time.sleep(3)
                    
                    placeholder.empty()

                for index, review in enumerate(reviews):
                    
                    with st.container():
                        st.markdown(f"Issue on Line {review['line']}")
                        
                        st.error(f"{review['line']} -> {review['roast']}")
                        
                        with st.expander(f"Fix for Line {review['line']}"):
                            st.write(f"**Why:** {review['fix_explanation']}")
                            st.code(review['fixed_code'], language='python')
                        
                        st.divider()
            else:
                st.error("The AI failed to return a valid list. Try again.")