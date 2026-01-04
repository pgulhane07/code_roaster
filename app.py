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
        with st.spinner("Analyzing your incompetence..."):
            
            
            data = get_roast_and_fix(user_code, persona)
            
            if "critiques" in data:
                reviews = data["critiques"]
                
               
                priority_map = {"fatal": 0, "warning": 1, "cosmetic": 2}
                reviews.sort(key=lambda x: priority_map.get(x["category"], 3))
                
                
                if any(r['category'] == 'fatal' for r in reviews):
                    placeholder = st.empty()
                    with placeholder.container():
                        st.markdown("<h1 style='text-align: center; color: red;'>💥 CRITICAL FAILURE DETECTED 💥</h1>", unsafe_allow_html=True)
                        st.markdown(
                            """
                            <div style="display: flex; justify-content: center;">
                                <img src="https://media.giphy.com/media/HhTXt43pk1I1W/giphy.gif" width="100%" style="max-width: 600px; border-radius: 10px;" />
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    
                    time.sleep(3.5)
                    placeholder.empty()

                for review in reviews:
                    cat = review['category']
                    
                    if cat == 'fatal':
                        container = st.error 
                        icon = "💥"
                        label = "CRITICAL FAILURE"
                    elif cat == 'warning':
                        container = st.warning
                        icon = "⛔"
                        label = "SYNTAX / BLOCKER"
                    else: 
                        container = st.success
                        icon = "💅"
                        label = "COSMETIC ISSUE"

                    container(f"**{icon} {label} (Line {review['line']}):** {review['roast']}")
                    
                    with st.expander(f"🛠️ Fix for Line {review['line']}"):
                        st.markdown(f"**Why:** {review['fix_explanation']}")
                        st.code(review['fixed_code'], language='python')
                    
                    st.write("") 

            else:
                st.error("The AI failed to return a valid list. Try again.")