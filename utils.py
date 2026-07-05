# ==========================================
# AI Career Score Calculator
# ==========================================

CAREER_SKILLS = {

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "NumPy",
        "Pandas",
        "Statistics",
        "Docker",
        "AWS"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "LangChain",
        "LLMs",
        "Prompt Engineering",
        "Docker",
        "AWS"
    ],

    "Data Analyst": [
        "Excel",
        "SQL",
        "Python",
        "Power BI",
        "Tableau",
        "Statistics",
        "Pandas"
    ],

    "Python Developer": [
        "Python",
        "OOP",
        "FastAPI",
        "Git",
        "Docker",
        "SQL"
    ],

    "Backend Developer": [
        "Python",
        "FastAPI",
        "SQL",
        "Docker",
        "Authentication",
        "AWS"
    ],

    "Cloud Engineer": [
        "Linux",
        "AWS",
        "Docker",
        "Kubernetes",
        "Terraform"
    ],

    "DevOps Engineer": [
        "Linux",
        "Docker",
        "Kubernetes",
        "Terraform",
        "Jenkins",
        "Git"
    ]
}


def calculate_score(user_skills, career):

    user_skills = [skill.strip().lower() for skill in user_skills]

    required = [
        skill.lower()
        for skill in CAREER_SKILLS.get(career, [])
    ]

    matched = [
        skill
        for skill in required
        if skill in user_skills
    ]

    score = int(len(matched) / len(required) * 100) if required else 0

    missing = [
        skill
        for skill in required
        if skill not in user_skills
    ]

    return score, missing

    # ==========================================
# Overall AI Career Score
# ==========================================

def calculate_overall_score(
    user_skills,
    career,
    resume_uploaded=False,
    roadmap_progress=0,
    project_progress=0
):

    skill_score, missing = calculate_score(
        user_skills,
        career
    )

    score = 0

    # Skills = 60 Marks
    score += skill_score * 0.60

    # Resume = 10 Marks
    if resume_uploaded:
        score += 10

    # Roadmap = 15 Marks
    score += roadmap_progress * 15

    # Projects = 15 Marks
    score += project_progress * 15

    return round(score), missing