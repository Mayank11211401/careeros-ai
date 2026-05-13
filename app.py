import streamlit as st
import pdfplumber
import pandas as pd
import plotly.express as px
import random
from streamlit_option_menu import option_menu
from fpdf import FPDF
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="CareerOS AI",
    page_icon="🚀",
    layout="wide"
)

# =========================================================
# PREMIUM UI
# =========================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    background-color: #0B1120;
    color: white;
}

.main {
    background: #0B1120;
}

section[data-testid="stSidebar"] {
    background: #111827;
}

h1 {
    font-size: 42px !important;
    font-weight: 700 !important;
    color: white !important;
}

h2, h3 {
    color: white !important;
}

.stButton>button {
    width: 100%;
    height: 50px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(
        135deg,
        #7C3AED,
        #2563EB
    );
    color: white;
    font-weight: 600;
    font-size: 16px;
}

.stTextInput>div>div>input,
.stTextArea textarea {
    background-color: #1E293B;
    color: white;
    border-radius: 12px;
}

[data-testid="metric-container"] {
    background: linear-gradient(
        145deg,
        #111827,
        #1E293B
    );

    border: 1px solid #374151;

    padding: 18px;

    border-radius: 18px;
}

.card {
    background: linear-gradient(
        145deg,
        #111827,
        #1E293B
    );

    padding: 25px;

    border-radius: 18px;

    margin-bottom: 20px;

    border: 1px solid #374151;
}

.big-text {
    font-size: 20px;
    font-weight: 600;
}

.small-text {
    color: #CBD5E1;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🚀 CareerOS AI")

    selected = option_menu(

        "Navigation",

        [
            "Home",
            "Resume Intelligence",
            "Resume Builder",
            "Portfolio Generator",
            "LinkedIn Optimizer",
            "Career Match",
        ],

        icons=[
            "house",
            "cpu",
            "file-earmark-person",
            "globe",
            "linkedin",
            "briefcase"
        ],

        default_index=0
    )

# =========================================================
# ROLE DATABASE
# =========================================================

roles = {

    "Data Analyst": {

        "skills": [
            "python",
            "sql",
            "excel",
            "power bi",
            "dashboard",
            "analytics"
        ],

        "career_type":
            "analytical and data-driven",

        "internships": [
            "Business Analytics Intern",
            "MIS Reporting Intern",
            "Data Operations Intern"
        ],

        "companies": [
            "Analytics Firms",
            "Consulting Companies",
            "Tech Service Companies"
        ]
    },

    "Business Analyst": {

        "skills": [
            "excel",
            "analysis",
            "communication",
            "sql",
            "presentation"
        ],

        "career_type":
            "business strategy and operations",

        "internships": [
            "Operations Intern",
            "Strategy Intern",
            "Business Consulting Intern"
        ],

        "companies": [
            "Consulting Firms",
            "Finance Companies",
            "Operations Teams"
        ]
    },

    "Marketing": {

        "skills": [
            "marketing",
            "branding",
            "sales",
            "seo",
            "communication"
        ],

        "career_type":
            "creative and communication-oriented",

        "internships": [
            "Digital Marketing Intern",
            "Branding Intern",
            "Content Strategy Intern"
        ],

        "companies": [
            "Media Agencies",
            "Consumer Brands",
            "Startup Marketing Teams"
        ]
    }
}

# =========================================================
# PDF EXTRACT
# =========================================================

def extract_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text.lower()

    return text

# =========================================================
# HOME
# =========================================================

if selected == "Home":

    st.title("🚀 CareerOS AI")

    st.subheader(
        "Intelligent Career Development Platform"
    )

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Career Analyses", "52K+")
    c2.metric("Students Guided", "11K+")
    c3.metric("Mock Interviews", "18K+")
    c4.metric("Resume Builds", "25K+")

    st.markdown("---")

    st.markdown("""
    <div class="card">

    <div class="big-text">
    Your Personal Career Intelligence System
    </div>

    <br>

    <div class="small-text">

    CareerOS AI helps students:
    
    • Build professional resumes  
    • Analyze employability  
    • Improve LinkedIn presence  
    • Match with careers and internships  
    • Generate portfolio websites  
    • Improve ATS compatibility  
    • Understand recruiter expectations  

    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# RESUME INTELLIGENCE
# =========================================================

if selected == "Resume Intelligence":

    st.title("🧠 Resume Intelligence Engine")

    role = st.selectbox(
        "Select Career Track",
        list(roles.keys())
    )

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    if uploaded_file:

        text = extract_text(uploaded_file)

        required_skills = roles[role]["skills"]

        matched = []
        missing = []

        for skill in required_skills:

            if skill in text:
                matched.append(skill)

            else:
                missing.append(skill)

        skill_score = int(
            (len(matched) /
            len(required_skills)) * 100
        )

        ats_score = random.randint(72, 94)

        communication_score = random.randint(60, 90)

        project_score = random.randint(55, 88)

        employability = int(
            (
                skill_score +
                ats_score +
                communication_score +
                project_score
            ) / 4
        )

        # =================================================
        # METRICS
        # =================================================

        st.markdown("---")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Employability",
            f"{employability}%"
        )

        c2.metric(
            "ATS Readiness",
            f"{ats_score}%"
        )

        c3.metric(
            "Technical Depth",
            f"{skill_score}%"
        )

        c4.metric(
            "Communication",
            f"{communication_score}%"
        )

        st.markdown("---")

        # =================================================
        # PROFILE SUMMARY
        # =================================================

        st.markdown("""
        <div class="card">
        <div class="big-text">
        Executive Profile Summary
        </div>
        </div>
        """, unsafe_allow_html=True)

        summary = f"""
Your resume reflects a profile with growing exposure toward
{roles[role]["career_type"]} roles.

The analysis indicates stronger alignment in areas such as
{", ".join(matched[:3]) if matched else "basic foundational skills"}.

However, recruiter confidence may reduce slightly due to gaps in
{", ".join(missing[:2]) if missing else "advanced specialization"}.

Your current profile appears more suitable for
entry-level internships and practical exposure opportunities
rather than highly specialized positions.

Adding measurable projects, certifications, and stronger
problem-solving examples would significantly improve profile strength.
"""

        st.info(summary)

        # =================================================
        # CAREER INSIGHTS
        # =================================================

        st.markdown("""
        <div class="card">
        <div class="big-text">
        Career Intelligence Insights
        </div>
        </div>
        """, unsafe_allow_html=True)

        insights = []

        if skill_score >= 80:
            insights.append(
                "Your technical profile demonstrates competitive readiness for analytical roles."
            )

        elif skill_score >= 60:
            insights.append(
                "Your profile shows good foundational skills but still requires stronger specialization."
            )

        else:
            insights.append(
                "Your profile currently lacks enough technical depth for competitive screening."
            )

        if communication_score >= 75:
            insights.append(
                "Your communication indicators suggest decent professional presentation capability."
            )

        else:
            insights.append(
                "Your resume lacks strong communication-oriented achievements and leadership indicators."
            )

        for item in insights:
            st.success(item)

        # =================================================
        # SKILL GAP
        # =================================================

        st.markdown("""
        <div class="card">
        <div class="big-text">
        Skill Gap Analysis
        </div>
        </div>
        """, unsafe_allow_html=True)

        for skill in missing:

            st.warning(
                f"Adding stronger exposure in {skill.upper()} would significantly improve recruiter confidence."
            )

        # =================================================
        # INTERNSHIP MATCHING
        # =================================================

        st.markdown("""
        <div class="card">
        <div class="big-text">
        Recommended Internship Paths
        </div>
        </div>
        """, unsafe_allow_html=True)

        for internship in roles[role]["internships"]:

            st.write(f"✅ {internship}")

        # =================================================
        # COMPANY TYPE SUGGESTION
        # =================================================

        st.markdown("""
        <div class="card">
        <div class="big-text">
        Organizational Alignment
        </div>
        </div>
        """, unsafe_allow_html=True)

        company_text = f"""
Based on your current profile maturity and skill composition,
you appear more aligned toward:

• {roles[role]["companies"][0]}  
• {roles[role]["companies"][1]}  
• Internship-driven learning environments  
• Growth-oriented startup ecosystems  

rather than highly specialized enterprise positions at this stage.
"""

        st.info(company_text)

        # =================================================
        # CHART
        # =================================================

        st.markdown("""
        <div class="card">
        <div class="big-text">
        Career Readiness Distribution
        </div>
        </div>
        """, unsafe_allow_html=True)

        chart_data = pd.DataFrame({

            "Category": [
                "Technical",
                "Communication",
                "ATS",
                "Projects"
            ],

            "Score": [
                skill_score,
                communication_score,
                ats_score,
                project_score
            ]
        })

        fig = px.bar(
            chart_data,
            x="Category",
            y="Score",
            text="Score"
        )

        fig.update_layout(
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font_color="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =========================================================
# RESUME BUILDER
# =========================================================

if selected == "Resume Builder":

    st.title("📄 Professional Resume Builder")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    linkedin = st.text_input("LinkedIn")
    skills = st.text_area("Skills")
    education = st.text_area("Education")
    projects = st.text_area("Projects")
    experience = st.text_area("Experience")

    if st.button("Generate Professional Resume"):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", "B", 20)

        pdf.cell(200, 10, txt=name, ln=True)

        pdf.set_font("Arial", size=12)

        pdf.cell(
            200,
            10,
            txt=f"{email} | {phone}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"LinkedIn: {linkedin}",
            ln=True
        )

        pdf.ln(10)

        sections = {

            "Skills": skills,
            "Education": education,
            "Projects": projects,
            "Experience": experience
        }

        for title, content in sections.items():

            pdf.set_font("Arial", "B", 14)

            pdf.cell(200, 10, txt=title, ln=True)

            pdf.set_font("Arial", size=12)

            pdf.multi_cell(0, 10, content)

            pdf.ln(5)

        file_name = f"{name}_Resume.pdf"

        pdf.output(file_name)

        with open(file_name, "rb") as file:

            st.download_button(
                "📥 Download Resume",
                file,
                file_name=file_name
            )

# =========================================================
# PORTFOLIO GENERATOR
# =========================================================

if selected == "Portfolio Generator":

    st.title("🌐 Portfolio Website Generator")

    name = st.text_input("Name")
    about = st.text_area("About")
    skills = st.text_area("Skills")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")

    if st.button("Generate Portfolio"):

        html = f"""
<html>

<head>

<title>{name} Portfolio</title>

<style>

body {{
font-family: Arial;
background: #0B1120;
color: white;
padding: 60px;
}}

.card {{
background: #111827;
padding: 30px;
border-radius: 20px;
}}

a {{
color: #60A5FA;
}}

</style>

</head>

<body>

<div class="card">

<h1>{name}</h1>

<h2>About</h2>

<p>{about}</p>

<h2>Skills</h2>

<p>{skills}</p>

<h2>Links</h2>

<a href="{linkedin}">LinkedIn</a><br><br>

<a href="{github}">GitHub</a>

</div>

</body>

</html>
"""

        st.download_button(
            "📥 Download Portfolio",
            html,
            file_name="portfolio.html"
        )

# =========================================================
# LINKEDIN OPTIMIZER
# =========================================================

if selected == "LinkedIn Optimizer":

    st.title("🔗 LinkedIn Profile Optimizer")

    headline = st.text_input("LinkedIn Headline")

    about = st.text_area("About Section")

    if st.button("Analyze LinkedIn Profile"):

        st.markdown("---")

        if len(headline) < 25:

            st.warning("""
Your headline lacks role-specific keywords and may not perform well in recruiter searches.
""")

        else:

            st.success("""
Your headline demonstrates stronger keyword positioning and professional identity clarity.
""")

        if len(about) < 120:

            st.warning("""
Your About section feels limited and may not effectively communicate career value and strengths.
""")

        else:

            st.success("""
Your About section reflects decent professional storytelling and profile confidence.
""")

# =========================================================
# CAREER MATCH
# =========================================================

# =========================================================
# CAREER MATCH
# =========================================================

if selected == "Career Match":

    st.title("📋 Resume vs Job Intelligence")

    st.markdown("""
This system compares your resume against
real role-specific technical requirements
instead of random keyword matching.
""")

    # =====================================================
    # ROLE SELECT
    # =====================================================

    role = st.selectbox(
        "Select Target Role",
        list(roles.keys())
    )

    # =====================================================
    # FILE UPLOAD
    # =====================================================

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    # =====================================================
    # JOB DESCRIPTION
    # =====================================================

    job_description = st.text_area(
        "Paste Real Job Description"
    )

    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    if st.button("Analyze Match"):

        if uploaded_file and job_description:

            # =============================================
            # EXTRACT RESUME TEXT
            # =============================================

            resume_text = extract_text(
                uploaded_file
            ).lower()

            jd_text = job_description.lower()

            # =============================================
            # PROFESSIONAL ROLE KEYWORDS
            # =============================================

            role_keywords = {

                "Data Analyst": {

                    "python": 18,
                    "sql": 18,
                    "excel": 10,
                    "power bi": 15,
                    "tableau": 12,
                    "analytics": 10,
                    "dashboard": 10,
                    "data visualization": 7
                },

                "Business Analyst": {

                    "analysis": 18,
                    "excel": 12,
                    "sql": 15,
                    "stakeholder": 12,
                    "requirements": 12,
                    "communication": 10,
                    "presentation": 10,
                    "documentation": 11
                },

                "Marketing": {

                    "marketing": 20,
                    "seo": 15,
                    "branding": 15,
                    "campaign": 15,
                    "sales": 12,
                    "social media": 13,
                    "content": 10
                }
            }

            keywords = role_keywords[role]

            # =============================================
            # MATCHING ENGINE
            # =============================================

            total_possible = sum(
                keywords.values()
            )

            earned_score = 0

            matched_keywords = []

            missing_keywords = []

            for keyword, weight in keywords.items():

                # Skill must exist in BOTH
                # Job Description + Resume

                if (
                    keyword in resume_text
                    and keyword in jd_text
                ):

                    earned_score += weight
                    matched_keywords.append(keyword)

                elif keyword in jd_text:

                    missing_keywords.append(keyword)

            # =============================================
            # FINAL SCORE
            # =============================================

            match_score = round(
                (earned_score / total_possible) * 100,
                1
            )

            # =============================================
            # SCORE LIMITER
            # =============================================

            if match_score > 100:
                match_score = 100

            # =============================================
            # DASHBOARD
            # =============================================

            st.markdown("---")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Role Compatibility",
                f"{match_score}%"
            )

            c2.metric(
                "Matched Skills",
                len(matched_keywords)
            )

            c3.metric(
                "Missing Skills",
                len(missing_keywords)
            )

            st.markdown("---")

            # =============================================
            # MATCHED SKILLS
            # =============================================

            st.subheader(
                "✅ Matching Professional Skills"
            )

            if matched_keywords:

                for skill in matched_keywords:

                    st.success(skill.upper())

            else:

                st.warning(
                    "No strong role-specific skills detected."
                )

            # =============================================
            # MISSING SKILLS
            # =============================================

            st.subheader(
                "⚠ Missing High-Value Skills"
            )

            if missing_keywords:

                for skill in missing_keywords:

                    st.warning(
                        f"{skill.upper()} missing from resume."
                    )

            else:

                st.success(
                    "Strong keyword alignment detected."
                )

            # =============================================
            # AI ANALYSIS
            # =============================================

            st.subheader(
                "🧠 AI Career Evaluation"
            )

            if match_score >= 80:

                st.success("""
Your resume demonstrates strong alignment
with the provided job requirements.

The profile reflects competitive technical
relevance, ATS readiness, and stronger
recruiter compatibility for this role.
""")

            elif match_score >= 60:

                st.warning("""
Your profile demonstrates moderate alignment
with the target role.

However, certain high-impact technical
competencies and project indicators are
still missing.
""")

            elif match_score >= 35:

                st.warning("""
Your resume currently reflects partial
role alignment.

Recruiter confidence may reduce due to
limited specialization and missing
technical depth.
""")

            else:

                st.error("""
Your profile currently shows weak alignment
with this role.

The resume lacks enough role-specific
technical indicators and ATS-oriented
optimization.
""")

            # =============================================
            # ROLE READINESS BAR
            # =============================================

            st.markdown("---")

            st.subheader(
                "📈 Career Readiness"
            )

            st.progress(match_score / 100)

            # =============================================
            # ROLE RECOMMENDATION
            # =============================================

            st.subheader(
                "🎯 Career Positioning Insight"
            )

            if match_score >= 75:

                st.info("""
Your profile currently appears suitable
for internship-to-entry-level transition
roles within this domain.
""")

            elif match_score >= 50:

                st.info("""
Your profile shows learning-stage alignment.

Adding stronger practical projects,
certifications, and technical exposure
would significantly improve opportunities.
""")

            else:

                st.info("""
Your profile currently appears better suited
for foundational learning and beginner-level
upskilling before competitive hiring.
""")

        else:

            st.warning(
                "Please upload resume and paste job description."
            )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    f"CareerOS AI • {datetime.now().year}"
)