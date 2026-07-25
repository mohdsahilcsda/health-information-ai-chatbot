import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load Environment Variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Health Information AI",
    page_icon="🍎",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#eef2ff,#ffffff,#e0f7fa);
}

/* Title */
.title{
    text-align:center;
    color:#0f172a;
    font-size:45px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#475569;
    font-size:18px;
}

/* Input Box */
textarea{
    border-radius:12px !important;
}

/* Button */
.stButton>button{
    width:100%;
    border-radius:12px;
    background:linear-gradient(90deg,#10b981,#059669);
    color:white;
    font-size:18px;
    font-weight:bold;
    padding:10px;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#059669,#047857);
    color:white;
}

/* Footer */
.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
    "<h1 class='title'>🍎 Health Information AI Chatbot</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p class='subtitle'>Your AI Assistant for Health Information & Healthcare Technology</p>",
    unsafe_allow_html=True,
)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
        width=120
    )

    st.header("📚 Topics Covered")

    st.success("""
✔ Health Information

✔ HMIS

✔ Medical Coding

✔ Billing

✔ Data Analytics

✔ AI in Healthcare

✔ Clinical Decision Support

✔ Health Data Security
""")

    st.info("⚠ This chatbot provides educational information only. It is NOT medical advice.")

# ---------------- INPUT ---------------- #

question = st.text_area(
    "💬 Ask Your Health Information Question",
    placeholder="Example: What is HMIS?"
)

# ---------------- PROMPT ---------------- #

prompt = ChatPromptTemplate.from_template("""
You are an expert in Health Information.

Answer ONLY health information related questions.

Topics:
- Health Information
- HMIS
- Medical Coding
- Billing
- Health Data Security
- AI in Healthcare
- Clinical Decision Support
- Data Analytics
- Electronic Health Records (EHR)
- Telemedicine
- Public Health Informatics

If the question is outside these topics reply:

"Sorry, I only answer Health Information related questions."

Question:
{question}

Provide:

1. Simple Explanation

2. Step-by-step Guidance

3. Best Practices

4. Precautions (if needed)

Answer in a clean, easy-to-read format.
""")

# ---------------- BUTTON ---------------- #

if st.button("🚀 Ask AI"):

    if question.strip() == "":
        st.warning("Please enter your question.")
    else:

        with st.spinner("🤖 AI is thinking..."):

            llm = ChatGroq(
                model="llama-3.1-8b-instant",
                temperature=0.3
            )

            chain = prompt | llm

            response = chain.invoke({
                "question": question
            })

        st.success("✅ Answer Generated")

        st.markdown("## 🤖 AI Response")

        st.write(response.content)

# ---------------- EXPANDER ---------------- #

with st.expander("ℹ About this Chatbot"):

    st.write("""
This chatbot can answer questions related to:

- Health Information
- Hospital Management Information Systems (HMIS)
- Electronic Health Records (EHR)
- Medical Coding & Billing
- Healthcare Data Analytics
- AI in Healthcare
- Clinical Decision Support Systems
- Health Data Security

❌ It does NOT answer unrelated topics.
""")

# ---------------- FOOTER ---------------- #

st.markdown(
    "<hr><p class='footer'>Made with ❤️ using Streamlit + LangChain + Groq</p>",
    unsafe_allow_html=True
)