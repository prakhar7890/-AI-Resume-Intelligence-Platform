import streamlit as st

from utils.file_reader import extract_text
from utils.llm import ask_llm
from utils.parser import prepare_resume_jd_prompt

from prompts.ats_prompt import ATS_PROMPT
from prompts.jd_match_prompt import JD_MATCH_PROMPT
from prompts.interview_prompt import INTERVIEW_PROMPT
from prompts.cover_letter_prompt import COVER_LETTER_PROMPT
from prompts.linkedin_prompt import LINKEDIN_PROMPT


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Resume Intelligence Platform",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.hero{
    background: linear-gradient(135deg,#0f172a,#1e293b);
    padding:2rem;
    border-radius:20px;
    color:white;
    text-align:center;
    margin-bottom:2rem;
}

.hero h1{
    font-size:3rem;
}

.hero p{
    color:#cbd5e1;
    font-size:1.1rem;
}

.stButton > button{
    width:100%;
    border-radius:12px;
    height:3rem;
    font-weight:bold;
}

.metric-card{
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero">
<h1> AI Resume Intelligence Platform</h1>
<p>
ATS Analysis • JD Matching • Interview Preparation • Cover Letters • LinkedIn Optimization
</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title(" Platform Features")
    st.markdown("""
    ➤ ATS Analysis

    ➤ Resume-JD Match

    ➤ Interview Questions

    ➤ Cover Letter Generator

    ➤ LinkedIn Optimizer
    """)

    st.divider()

    st.info(
        "Upload Resume and Job Description to unlock all modules."
    )

# =====================================================
# DASHBOARD
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "ATS",
        "Ready"
    )

with col2:
    st.metric(
        "JD Match",
        "Ready"
    )

with col3:
    st.metric(
        "Interview",
        "Ready"
    )

with col4:
    st.metric(
        "LinkedIn",
        "Ready"
    )

st.divider()

# =====================================================
# FILE UPLOADS
# =====================================================

col1, col2 = st.columns(2)

with col1:

    resume_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf", "docx", "txt"]
    )

with col2:

    jd_file = st.file_uploader(
        "💼 Upload Job Description",
        type=["pdf", "docx", "txt"]
    )

resume_text = None
jd_text = None

if resume_file:

    resume_text = extract_text(
        resume_file
    )

    st.success(
        f"➤ Resume Uploaded: {resume_file.name}"
    )

if jd_file:

    jd_text = extract_text(
        jd_file
    )

    st.success(
        f"➤ JD Uploaded: {jd_file.name}"
    )

# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📄 ATS Analysis",
    "🎯 JD Match",
    "🎤 Interview Prep",
    "✉️ Cover Letter",
    "💼 LinkedIn"
])

# =====================================================
# ATS TAB
# =====================================================

with tab1:

    if resume_text:

        if st.button("Analyze Resume"):

            with st.spinner(
                "Analyzing Resume..."
            ):

                result = ask_llm(
                    ATS_PROMPT,
                    resume_text
                )

                st.success(
                    "ATS Analysis Completed"
                )

                st.markdown(result)

                st.download_button(
                    "⬇ Download ATS Report",
                    result,
                    file_name="ATS_Report.txt"
                )

    else:

        st.info(
            "Upload a Resume first."
        )

# =====================================================
# JD MATCH TAB
# =====================================================

with tab2:

    if resume_text and jd_text:

        combined_prompt = prepare_resume_jd_prompt(
            resume_text,
            jd_text
        )

        if st.button(
            "Generate JD Match Report"
        ):

            with st.spinner(
                "Matching Resume with JD..."
            ):

                result = ask_llm(
                    JD_MATCH_PROMPT,
                    combined_prompt
                )

                st.success(
                    "Match Analysis Completed"
                )

                st.markdown(result)

                st.download_button(
                    "⬇ Download Match Report",
                    result,
                    file_name="JD_Match_Report.txt"
                )

    else:

        st.info(
            "Upload both Resume and Job Description."
        )

# =====================================================
# INTERVIEW TAB
# =====================================================

with tab3:

    if resume_text and jd_text:

        combined_prompt = prepare_resume_jd_prompt(
            resume_text,
            jd_text
        )

        if st.button(
            "Generate Interview Questions"
        ):

            with st.spinner(
                "Generating Questions..."
            ):

                result = ask_llm(
                    INTERVIEW_PROMPT,
                    combined_prompt
                )

                st.success(
                    "Questions Generated"
                )

                st.markdown(result)

                st.download_button(
                    "⬇ Download Questions",
                    result,
                    file_name="Interview_Questions.txt"
                )

    else:

        st.info(
            "Upload both Resume and Job Description."
        )

# =====================================================
# COVER LETTER TAB
# =====================================================

with tab4:

    if resume_text and jd_text:

        combined_prompt = prepare_resume_jd_prompt(
            resume_text,
            jd_text
        )

        if st.button(
            "Generate Cover Letter"
        ):

            with st.spinner(
                "Generating Cover Letter..."
            ):

                result = ask_llm(
                    COVER_LETTER_PROMPT,
                    combined_prompt
                )

                st.success(
                    "Cover Letter Generated"
                )

                st.markdown(result)

                st.download_button(
                    "⬇ Download Cover Letter",
                    result,
                    file_name="Cover_Letter.txt"
                )

    else:

        st.info(
            "Upload both Resume and Job Description."
        )

# =====================================================
# LINKEDIN TAB
# =====================================================

with tab5:

    if resume_text:

        if st.button(
            "Generate LinkedIn Profile"
        ):

            with st.spinner(
                "Optimizing LinkedIn..."
            ):

                result = ask_llm(
                    LINKEDIN_PROMPT,
                    resume_text
                )

                st.success(
                    "LinkedIn Content Generated"
                )

                st.markdown(result)

                st.download_button(
                    "⬇ Download LinkedIn Content",
                    result,
                    file_name="LinkedIn_Profile.txt"
                )

    else:

        st.info(
            "Upload a Resume first."
        )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
### 🛠 Built With

- Streamlit
- Hugging Face
- Qwen 2.5
- Python

**Developed by Prakhar Gupta**
""")
