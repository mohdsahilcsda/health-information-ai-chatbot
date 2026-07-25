import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Health Information AI",
    page_icon="🩺",
    layout="wide",
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

body{
    background-color:#F4F8FB;
}

.main{
    background:#F4F8FB;
}

.header{
    padding:30px;
    border-radius:18px;
    background:linear-gradient(90deg,#00B894,#0984E3);
    color:white;
    text-align:center;
    margin-bottom:20px;
    box-shadow:0px 8px 20px rgba(0,0,0,.15);
}

.question-box{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,.08);
}

.answer-box{
    background:#ffffff;
    border-left:8px solid #00B894;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 5px 15px rgba(0,0,0,.08);
}

.topic{
    background:#E8F8F5;
    padding:10px;
    border-radius:8px;
    margin-bottom:8px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/480/health-book.png",
        width=120
    )

    st.title("Health AI")

    st.markdown("---")

    st.subheader("📚 Topics Covered")

    st.markdown("""
✅ Health Information

✅ Health Information Systems

✅ Medical Coding & Billing

✅ Clinical Decision Support

✅ Data Analytics

✅ HMIS

✅ AI in Healthcare

✅ Health Data Security
""")

    st.markdown("---")

    st.info(
        "This chatbot answers only Health Information related questions."
    )

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="header">

<h1>🩺 Health Information AI Chatbot</h1>

<p>
Professional AI Assistant for Health Information,
Medical Coding, HMIS, Data Security,
Clinical Decision Support and Healthcare Analytics.
</p>

</div>
""", unsafe_allow_html=True)

# ---------------- TWO COLUMNS ---------------- #

left, right = st.columns([2.5,1])

# LEFT

with left:

    st.markdown("### 💬 Ask Your Question")

    question = st.text_area(
        "",
        height=180,
        placeholder="Example: What is HMIS?"
    )

    ask = st.button(
        "🚀 Ask AI",
        use_container_width=True
    )

# RIGHT

with right:

    st.markdown("### 💡 Example Questions")

    st.success("""
• What is Health Information?

• Explain HMIS.

• Importance of Medical Coding.

• AI in Healthcare.

• Clinical Decision Support System.

• Health Data Security.

• Explain Medical Billing.
""")

# ---------------- PROMPT ---------------- #

prompt = ChatPromptTemplate.from_template("""
You are a Health Information Expert.

Answer ONLY Health Information related questions.

Topics include:

- Health Information
- Health Information Systems
- Medical Coding
- Medical Billing
- Health Data Security
- Healthcare Analytics
- AI in Healthcare
- Clinical Decision Support
- HMIS
- Electronic Health Records

If the question is outside these topics, reply exactly:

"❌ Sorry, I only answer Health Information related questions."

Question:
{question}

Your response format:

## 📖 Simple Explanation

## 🪜 Step-by-Step Guidance

## ✅ Best Practices

## ⚠️ Precautions (if applicable)

Use markdown formatting.
""")

# ---------------- LLM ---------------- #

if ask:

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    chain = prompt | llm

    with st.spinner("🧠 AI is thinking..."):

        response = chain.invoke({
            "question": question
        })

    st.markdown("## 🤖 AI Response")

    st.markdown(
        f"""
<div class="answer-box">

{response.content}

</div>
""",
        unsafe_allow_html=True
    )

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.caption(
    "Developed with ❤️ using Streamlit • LangChain • Groq • Llama 3.1"
)